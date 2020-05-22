import React from 'react';

import Aux from '../hoc/Auxiliary';
import Dashboard from './SportsDashboard/SportsDashboard';

const sports = (props) => {
    const data = props.data;
    console.log(data);
    let ele = null;
    let dash = [];
    for (let key in data){
        if(key === 'nba' || key === 'soccer'){ /// 
        ele = <Dashboard
            title={key}
            data={data[key]}
        />
        dash.push(ele)
        };
    };
    
    return ( 
        <Aux>
            {dash}
        </Aux>

     );
}
 
export default sports;


//NBA - scoreboard, standings, leaders (toggleable)
// EPL - "scoreboard"/fixtures, standings, scoring leaders
//NFL - scoreboard