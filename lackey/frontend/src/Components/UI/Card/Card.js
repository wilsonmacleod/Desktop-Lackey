import React from 'react';

import './Card.css';

const card = (props) => {
    return ( 
        <div className={`card ${props.cardType}`}>
            <div className="card-header">{props.header}</div>
            <div className="card-content">
                {props.children}
            </div>
        </div>
     );
}
 
export default card;