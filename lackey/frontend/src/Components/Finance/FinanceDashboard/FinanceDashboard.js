import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Button from '../../UI/Button/Button';
import Card from '../../UI/Card/Card';

import './FinanceDashboard.css';

const dashboard = (props) => {
    let transactions = "You have no transactions for this fund at this time...";
    if(props.transactions.length > 0){
        transactions = "Transactions Woo Hoo";
        };
    return ( 
        <Aux>
        <h3 className="dash-title">{props.title}</h3>
            <div className="f-container">
                <div className="figure-container">
                    {props.figure}
                </div>
                <Card cardType="data-container"
                    header={<div className="head-sub">
                        <div className="c-title">Data</div>
                        </div>}
                >
                    Data Component
                </Card>
                <Card cardType="trans-container"
                    header={
                        <div className="head-sub">
                            <div className="c-title">Transactions</div>
                        <Button btnType={"submit"} val={'investmentFund'} clicked={() => console.log('hello')}><i className="fa fa-plus" aria-hidden="true"></i></Button>
                        </div>}
                >
                    {transactions}
                </Card>
            </div>
            <span className="text">Last Updated: {props.updated}</span>
            <Button btnType={"submit"} clicked={props.refreshFund} val={props.title}>Refresh</Button>
            <Button btnType={"remove"} clicked={props.removeFund} val={props.title}>Remove</Button>
          </Aux>
     );
}
 
export default dashboard;