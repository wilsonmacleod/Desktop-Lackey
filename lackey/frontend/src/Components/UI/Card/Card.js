import React from 'react';

import './Card.css';

const card = (props) => {
    let cssClass = props.cardType !== undefined ? props.cardType : "card";
    console.log(cssClass)
    return ( 
        <div className={cssClass}>
            <div className="card-header">{props.header}</div>
            <div className="card-content">
                {props.children}
            </div>
        </div>
     );
}
 
export default card;