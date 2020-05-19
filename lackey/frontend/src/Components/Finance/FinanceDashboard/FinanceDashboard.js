import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Button from '../../UI/Button/Button';
import Card from '../../UI/Card/Card';

import './FinanceDashboard.css';

const dashboard = (props) => {
    return ( 
        <Aux>
        <h3 className="dash-title">{props.title}</h3>
            <div className="f-container">
                <div className="figure-container">
                    {props.figure}
                </div>
                <Card cardType="data-container"
                    header={"Data Component"}
                >
                    Data Component
                </Card>
                <Card cardType="trans-container"
                    header={"Transaction Component"}
                >
                    Transaction Component
                </Card>
            </div>
            <span className="text">Last Updated: {props.updated}</span>
            <Button btnType={"submit"} clicked={props.refreshFund} val={props.title}>Refresh</Button>
            <Button btnType={"remove"} clicked={props.removeFund} val={props.title}>Remove</Button>
          </Aux>
     );
}
 
export default dashboard;