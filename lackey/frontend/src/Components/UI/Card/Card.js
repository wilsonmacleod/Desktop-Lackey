import React from 'react';

import './Card.css';

const card = (props) => {
    let cssClass = props.cardType !== undefined ? props.cardType : "card";
    let header = props.header !== 'null' ? 
    <div className="card-header">{props.header}</div> :
    null;    return ( 
        <div className={cssClass}>
            {header}
            <div className="card-content">
                {props.children}
            </div>
        </div>
     );
}
 
export default card;