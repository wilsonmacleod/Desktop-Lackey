import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Nba from './Nba/Nba';
import Soccer from './Soccer/Soccer';

import './SportsDashboard.css';

const sportsDashboard = (props) => {
    const contents = {
        'nba': <Nba 
                    data ={props.data}
                />,
        'soccer': <Soccer 
                    data={props.data}
                 />
    }
    let content = contents[props.title];
    return ( 
        <Aux>
            <h3 className="dash-title">{props.title.toUpperCase()}</h3>
            <div className="s-container">
                {content}
            </div>     
        </Aux>
     );
}
 
export default sportsDashboard;