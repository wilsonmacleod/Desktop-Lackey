import React from 'react';

import Aux from '../hoc/Auxiliary';
import Dashboard from './SportsDashboard/SportsDashboard';
import Scoreboard from './Scoreboard/Scoreboard';

const sports = (props) => {
    const data = props.data;
    let ele = null;
    let dash = [];
    let scoreboard = {};
    for (let key in data){
        if(key === 'nba' || key === 'soccer'){ /// 
        ele = <Dashboard
            title={key}
            data={data[key]}
        />
        dash.push(ele)
        };
        scoreboard[`${key}`] = data[key].scoreboard;
    };
    let scoreboardDash = <Scoreboard
                            title={'Games'}
                            data={scoreboard}
                        />

    return ( 
        <Aux>
            {scoreboardDash}
            {dash}
        </Aux>

     );
}
 
export default sports;
