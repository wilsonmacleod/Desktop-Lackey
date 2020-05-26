import React from 'react';

import Aux from '../../../hoc/Auxiliary';
import Table from '../../../UI/Table/Table';

const soccerScoreboard = (props) => {
    const data = props.data;
    let matches = data.map(i => {
        let date = i.data.date;
        let status = i.data.status;
            return <div className="sbInfo">
                            <Table
                                headers={[`${date} (Day: ${i.matchday})`, status]}  
                                contents={
                                <Aux>
                                    <tr key={i.home_team}>
                                        <td className="team-name"><u>{i.home_team}</u></td>
                                        <td className="team">{i.data.fullTime.home}</td>
                                    </tr>
                                    <tr key={i.away_team}>
                                        <td className="team-name"><u>{i.away_team}</u></td>
                                        <td className="team">{i.data.fullTime.away}</td>
                                    </tr>
                                </Aux>
                                }
                            />
                    </div>
    });
    return ( 
        <div className="scoreboard-container">
            {matches}
        </div>
     );
}
 
export default soccerScoreboard;