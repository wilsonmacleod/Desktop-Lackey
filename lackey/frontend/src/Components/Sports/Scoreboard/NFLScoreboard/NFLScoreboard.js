import React from 'react';

const nflScoreboard = (props) => {
    const data = props.data;
    let soccer = data.map(i => {
    return  <div className="sbInfo">
                <div className="teamDiv">
                    <p>{i.time_date}</p>
                    <p><img className="contain" src={i.home_team_logo} alt=''/> <u>{i.home_team}</u></p>
                </div>
                <div className="scoreDiv">
                    <p>{i.data.home_team_score}</p>
                </div>
                <div className="teamDiv">
                    <p><u>{i.away_team}</u></p>
                    <p>{i.data.odds}</p>
                </div>
                <div className="scoreDiv">
                    <p>{i.data.away_team_score}</p>
                </div>
            </div>
        });
    return ( 
        <div className="scoreboard-container">
            <div className="bannerDiv">
                <p>Week: {props.data[0].current_week}</p>
            </div>
            {soccer}
        </div>
     );
}
 
export default nflScoreboard;