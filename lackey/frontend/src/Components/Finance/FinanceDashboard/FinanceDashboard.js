import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Button from '../../UI/Button/Button';
import Card from '../../UI/Card/Card';
import Figure from './Figure/Figure';
import Information from './Information/Information';
import Transactions from './Transactions/Transactions';

import './FinanceDashboard.css';

const dashboard = (props) => {
    return ( 
        <Aux>
        <h3 className="dash-title">{props.title}</h3>
            <div className="f-container">
                <div className="figure-container">
                    <Figure 
                        data={props.data}
                        key={props.title}
                    /> 
                </div>
                <Card cardType="data-container"
                    header={<div className="head-sub">
                        <div className="c-title">Information</div>
                        </div>}
                >
                    <Information
                        data={props.data}
                    />
                </Card>
                <Card cardType="trans-container"
                    header={
                        <div className="head-sub">
                            <div className="c-title">Transactions</div>
                        <Button btnType={"submit"} val={props.title} clicked={props.modalHandler}><i className="fa fa-plus" aria-hidden="true"></i></Button>
                        </div>}
                >
                    <Transactions
                        data={props.transactions}
                        removeTransaction={props.removeTransaction}
                    />
                </Card>
            </div>
            <span className="text">Last Updated: {props.updated}</span>
            <Button btnType={"submit"} clicked={props.refreshFund} val={props.title}>Refresh</Button>
            <Button btnType={"remove"} clicked={props.removeFund} val={`config=${props.title}`}>Remove</Button>
          </Aux>
     );
}
 
export default dashboard;