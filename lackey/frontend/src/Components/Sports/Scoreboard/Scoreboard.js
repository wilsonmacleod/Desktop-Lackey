import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Nba from './NbaScoreboard/NbaScoreboard';
import Soccer from './SoccerScoreboard/SoccerScoreboard';
import Nfl from './NFLScoreboard/NFLScoreboard';

import './Scoreboard.css';

const scoreboard = (props) => {
    const data = props.data;
    return ( 
        <Aux>
            <h3 className="dash-title">{props.title.toUpperCase()}</h3>
            <div className="s-container">
                    <Nfl 
                        data={data.nfl}
                    />
                    <Soccer
                        data={data.soccer}
                    />
                    <Nba 
                        data={data.nba}
                    />
            </div>      
        </Aux>
    );
}
 
export default scoreboard;
