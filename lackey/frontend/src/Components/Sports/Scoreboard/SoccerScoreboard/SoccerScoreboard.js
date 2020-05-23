import React from 'react';

const soccerScoreboard = (props) => {
    const data = props.data;
    let soccer = data.map(i => {
    return  <div className="sbInfo">
                <div className="teamDiv">
                    <p><u>{i.home_team}</u></p>
                </div>
                <div className="scoreDiv">
                    <p>{i.data.fullTime.home}</p>
                </div>
                <div className="teamDiv">
                    <p><u>{i.away_team}</u></p>
                </div>
                <div className="scoreDiv">
                    <p>{i.data.fullTime.away}</p>
                </div>
            </div>
        });
    return ( 
        <div className="scoreboard-container">
            {/*<div className="bannerDiv">
                <p>Matchday: {props.data[0].matchday}</p>
    </div>*/}
            {soccer}
        </div>
     );
}
 
export default soccerScoreboard;