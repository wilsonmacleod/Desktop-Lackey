import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Button from '../../UI/Button/Button';

import Nba from './NbaScoreboard/NbaScoreboard';
import Soccer from './SoccerScoreboard/SoccerScoreboard';
import Nfl from './NFLScoreboard/NFLScoreboard';

import './Scoreboard.css';

const scoreboard = (props) => {
    const data = props.data;
    return ( 
        <Aux>
            <h3 className="dash-title">Scores</h3>
            <h3 className="dash-title-nba">NBA</h3>
            <h3 className="dash-title-epl">EPL</h3>
            <h3 className="dash-title-nfl">NFL</h3>
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
            <Button btnType={"submit"} clicked={props.refreshScoreboard} val={'scoreboard'}>Refresh</Button>
        </Aux>
    );
}
 
export default scoreboard;
