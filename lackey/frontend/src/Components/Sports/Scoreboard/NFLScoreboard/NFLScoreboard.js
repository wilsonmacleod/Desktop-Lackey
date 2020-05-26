import React from 'react';

import Aux from '../../../hoc/Auxiliary';
import Table from '../../../UI/Table/Table';

const nflScoreboard = (props) => {
    const data = props.data;
    let key = 0;
    let games = data.map(i => {
        let qtr = i.data.qtr;
        let rem = i.data.rem_time;
        let odds = i.data.odds;
        let time_date = i.time_date.substring(0, i.time_date.length-15);
        key++;
        return <div className="sbInfo-nfl">
                        <Table
                            headers={[`${time_date}`, `QTR: ${qtr} ${rem}`]}
                            contents={
                            <Aux>
                                <tr key={i.current_week}>
                                    <td>Week: {i.current_week} {i.season}</td>
                                </tr>
                                <tr key={key}>
                                    <td>Favorite: <b>{odds}</b></td>
                                </tr>
                                <tr key={i.home_team}>
                                    <td><img className="contain" src={i.data.home_team_logo} alt=''/> <u>{i.home_team}</u></td>
                                    <td className="team-name">{i.data.home_team_score}</td>
                                </tr>
                                <tr key={i.away_team}>
                                    <td><img className="contain" src={i.data.away_team_logo} alt=''/> <u>{i.away_team}</u></td>
                                    <td className="team-name">{i.data.away_team_score}</td>
                                </tr>
                            </Aux>
                            }
                        />
                </div>
    });
    return ( 
        <div className="scoreboard-container">
            {games}
        </div>
     );
}
 
export default nflScoreboard;