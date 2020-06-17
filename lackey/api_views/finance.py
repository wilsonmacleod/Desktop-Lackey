import json
import datetime
import locale

from flask import jsonify
from flask_restful import Resource

from lackey import logger
from lackey.models import db, FinanceConfig, FinanceTempStore, FinanceInvestment
from lackey.external_apis import finance

class FINANCE(Resource): # /Finance/<arg> (None if none)
    def get(self, arg):
        if arg == 'init':
            config = FinanceConfig.query.all()
            if config != []:
                data = Actions.updateNeeded(config)
            else:
                data = 'None'
        else:
            arg = arg.split('=')
            keyword, query = arg[0], arg[1]
            if keyword == 'query':
                data = finance.search_fund(query)
            elif keyword == 'refresh':
                obj = FinanceConfig.query.filter_by(stock_symbol=query).first()
                Actions.delete(obj.stock_symbol)
                data = Actions.update(obj.stock_symbol)
        logger.debug(f'get.FINANCE: {data}')
        return jsonify(status=200, text={'data': f'{data}'})

    def post(self, arg):
        j = json.loads(arg)
        try: # if post is config
            if j['name']:
                new = FinanceConfig(
                    stock_symbol=j['stock_symbol'],
                    name=j['name']
                )
        except KeyError: # if post is investment transaction
            new = FinanceInvestment(
                stock_symbol=j['stockSymbol'],
                shares_count=j['shareCount'],
                price_per_share=j['pricePerShare'],
                date=j['date']
            )
        logger.debug(f'FINANCE.POST: {new}')
        db.session.add(new)
        db.session.commit()
        return jsonify(status=200)

    def delete(self, arg):
        arg = arg.split('=')
        item = ''
        if arg[0] == 'config':
            item = FinanceConfig.query.filter_by(stock_symbol=arg[1]).first()
            db.session.delete(item)
            cascade = FinanceTempStore.query.filter_by(stock_symbol=item.stock_symbol).all()
            for each in cascade:
                db.session.delete(each)
        elif arg[0] == 'transaction':
            item = FinanceInvestment.query.filter_by(id=arg[1]).first()
            db.session.delete(item)
        db.session.commit()
        logger.debug(f'FINANCE.DELETE: {item}')
        return jsonify(status=200)

class Actions():
    def updateNeeded(config):
        data = {'data': {}, 'transactions': {}}
        for each in config:
            stock_symbol = each.stock_symbol
            check = FinanceTempStore.query.filter_by(stock_symbol=stock_symbol).first()

            if not check: # if nothing in db
                data['data'][stock_symbol] = (Actions.update(stock_symbol))
                data['transactions'][stock_symbol] = (Actions.update_investment(stock_symbol, data))

            elif check and Actions.checkDate(check): # if ood in db
                Actions.delete(stock_symbol)
                data['data'][stock_symbol] = (Actions.update(stock_symbol))
                data['transactions'][stock_symbol] = (Actions.update_investment(stock_symbol, data))

            else: # if already updated
                data['data'][stock_symbol] = (Actions.dontUpdate(stock_symbol))
                data['transactions'][stock_symbol] = (Actions.update_investment(stock_symbol, data))
                
        return data

    def checkDate(check):
        logger.debug('checkDate')
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')   
        entered = check.entered_date
        hour_ahead = entered + datetime.timedelta(hours=1)
        now = datetime.datetime.now()
        if now > hour_ahead:
            logger.debug('checkDate-true')
            return True
        return False

    def delete(stock_symbol): # for refresh
        logger.debug('delete')
        objs = FinanceTempStore.__table__.delete().where(FinanceTempStore.stock_symbol == stock_symbol)
        db.session.execute(objs)
        db.session.commit()

    def update(stock_symbol, data_class='default'):
        #logger.debug('update')
        new_data = finance.get(data_class, stock_symbol)
        for i in new_data:
            logger.debug(i)
            new = FinanceTempStore(
                    stock_symbol=i['stock_symbol'],
                    date=i['date'],
                    opening=i['open'],
                    high=i['high'],
                    low=i['low'],
                    close=i['close'],
                    change=i['change']
                        )
            db.session.add(new)
            db.session.commit()
        return new_data

    def calculate_performace(initial, current):
        if current > initial:
            x = '+'
            change = (((current - initial) / initial) *  100)
        else:
            x = '-'
            change = (((initial - current) / initial) *  100)
        change = f'{x},{round(change, 2)}'
        return change

    def update_investment(stock_symbol, data):
        logger.debug(f'update_investment')
        try:
            newest_value = data['data'][stock_symbol][0].close
        except:
            newest_value = data['data'][stock_symbol][0]['close']
        funds = FinanceInvestment.query.filter_by(stock_symbol=stock_symbol).all()
        if funds:
            total = {
                    'type': 'total',
                    'shares_count': 0,
                    'initial': 0,
                    'current': 0,
                }
            new_data = []
            for each in funds:
                initial = int(each.shares_count * each.price_per_share)
                current = int(each.shares_count * newest_value)
                change = Actions.calculate_performace(initial, current)
                new_data.append({
                    'type': 'single',
                    'id': each.id,
                    'shares_count': each.shares_count,
                    'buy_price': each.price_per_share,
                    'initial': initial,
                    'current': current,
                    'change': change,
                    'date': each.date
                })
                total['shares_count'] += each.shares_count
                total['initial'] += initial
                total['current'] += current
            total['change'] = Actions.calculate_performace(total['initial'] , total['current'])
            new_data
            new_data.insert(0, total)
        else:
            new_data = ''
        return new_data

    def dontUpdate(stock_symbol):
        logger.debug('dontUpdate')
        return FinanceTempStore.query.filter_by(stock_symbol=stock_symbol).all()