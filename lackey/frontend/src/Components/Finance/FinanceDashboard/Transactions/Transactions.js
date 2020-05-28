import React from 'react';

import Aux from '../../../hoc/Auxiliary';
import Button from '../../../UI/Button/Button';

import '../FinanceDashboard.css';

const transactions = (props) => {
    const data = props.data;
    let transactions = 
        <div className="info-container">
            <p><u><strong>No Transactions</strong></u></p>
        </div>
    if(data.length > 0){
        transactions = [];
        for(let x = 0; x < data.length; x++){
            if(data[x]['type'] === 'total'){
                let change = data[x].change.split(',');
                let sign= change[0];
                let perc = change[1];
                let changeCss = sign === '+' ? "increase" : "decrease";
                let ele = 
                <div className="total-container">
                    <p><u><strong>Total</strong></u></p>
                    <p>Current Value: $<strong>{data[x].current}</strong></p>
                    <p>Initial Value: $<strong>{data[x].initial}</strong></p>
                    <p>Performance: <span className={changeCss}> {perc}{sign}</span>%</p>
                    <p>Total Shares Owned: <strong>{data[x].shares_count}</strong></p>
                </div>
                transactions.push(ele)
            }else{
                let change = data[x].change.split(',');
                let sign= change[0];
                let perc = change[1];
                let changeCss = sign === '+' ? "increase" : "decrease";
                let ele =
                <div className="info-container">
                    <Button 
                        clicked={props.removeTransaction} 
                        val={`transaction=${data[x].id}`}
                        btnType={'deleteTask'}>
                        <i val={`transaction=${data[x].id}`} className="fa fa-minus" aria-hidden="true" />
                        </Button>
                    <p><u><strong>{data[x].date}</strong></u></p>
                    <p>Buy Price: $<strong>{data[x].initial}</strong></p>
                    <p>Current Value: $<strong>{data[x].current}</strong></p>
                    <p>Performance: <span className={changeCss}> {perc}{sign}</span>%</p>
                    <p>Per Share: $<strong>{data[x].buy_price}</strong></p>
                    <p>Shares: <strong>{data[x].shares_count}</strong></p>
                </div>
                transactions.push(ele)
            }
        }
    };
    return ( 
        <Aux>
            {transactions}
        </Aux>
     );
}
 
export default transactions;