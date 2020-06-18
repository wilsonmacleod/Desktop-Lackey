import React from 'react';

import Button from '../../UI/Button/Button';

import './FinanceSearchResult.css';

const financeSearchResult = (props) => {
    return ( 
        <div className="result">
            <p className="name">{props.name}</p>
            <p className="text">{props.symbol}</p>
            <p className="text">{props.type}</p>
            <p className="text">{props.currency}</p>
            <p>
            <Button
                val={[props.symbol, props.name]}
                clicked={props.addFund}
                btnType={"addLoc"}>
                    <div><b>+</b></div>
            </Button>
            </p>
    </div>
     );
}
 
export default financeSearchResult;