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
        new = FinanceConfig(
            stock_symbol=j['stock_symbol'],
            name=j['name']
        )
        logger.debug(f'FINANCE.POST: {new}')
        db.session.add(new)
        db.session.commit()
        return jsonify(status=200)

    def delete(self, arg):
        config = FinanceConfig.query.filter_by(stock_symbol=arg).first()
        db.session.delete(config)
        cascade = FinanceTempStore.query.filter_by(stock_symbol=config.stock_symbol).all()
        for each in cascade:
            db.session.delete(each)
        db.session.commit()
        logger.debug(f'FINANCE.DELETE: {config}')
        return jsonify(status=200)

class Actions():
    def updateNeeded(config):
        data = {'data': {}, 'transactions': {}}
        for each in config:
            stock_symbol = each.stock_symbol
            check = FinanceTempStore.query.filter_by(stock_symbol=stock_symbol).first()

            if not check: # if nothing in db
                data['data'][stock_symbol] = (Actions.update(stock_symbol))
                data['transactions'][stock_symbol] = FinanceInvestment.query.filter_by(stock_symbol=stock_symbol).all()

            elif check and Actions.checkDate(check): # if ood in db
                Actions.delete(stock_symbol)
                data['data'][stock_symbol] = (Actions.update(stock_symbol))
                data['transactions'][stock_symbol] = FinanceInvestment.query.filter_by(stock_symbol=stock_symbol).all()

            else: # if already updated
                data['data'][stock_symbol] = (Actions.dontUpdate(stock_symbol))
                data['transactions'][stock_symbol] = FinanceInvestment.query.filter_by(stock_symbol=stock_symbol).all()
                
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

    def update(stock_symbol):
        #logger.debug('update')
        new_data = finance.get('default', stock_symbol)
        for i in new_data:
            logger.debug(i)
            new = FinanceTempStore(
                    stock_symbol=i['stock_symbol'],
                    date=i['date'],
                    opening=i['open'],
                    high=i['high'],
                    low=i['low'],
                    close=i['close'],
                        )
            db.session.add(new)
            db.session.commit()
        return new_data

    def dontUpdate(stock_symbol):
        logger.debug('dontUpdate')
        return FinanceTempStore.query.filter_by(stock_symbol=stock_symbol).all()