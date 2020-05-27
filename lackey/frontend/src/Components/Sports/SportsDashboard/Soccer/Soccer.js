import React from 'react';

import Aux from '../../../hoc/Auxiliary';
import Table from '../../../UI/Table/Table';

import '../SportsDashboard.css';


const soccer = (props) => {
    const data = props.data;
    let standingsHeaders = [
        'Team', 'Matches', 'Won', 
        'Lost', 'Draw', 'PTS', 'GF', 'GA',
        'GD'
        ];
    let standings = data.standings.map(i => {
            return <tr key={i.rank}>
            <td><img src={i.crest} className="contain" alt=''/> {i.team}</td>
            <td>{i.data.playedGames}</td>
            <td>{i.data.won}</td>
            <td>{i.data.lost}</td>
            <td>{i.data.draw}</td>
            <td>{i.data.points}</td>
            <td>{i.data.goalsFor}</td>
            <td>{i.data.goalsAgainst}</td>
            <td>{i.data.goalDifference}</td>
        </tr>
    }); 
    let leaderHeaders = ['Name', 'Nationality', 'Team', 'Goals'];
    let leaders = data.leaders.map(i => {
        return <tr key={i.name}>
        <td>{i.name}</td>
        <td>{i.nationality}</td>
        <td>{i.team}</td>
        <td>{i.number_goals}</td>
    </tr>
}); 
        
    return ( 
        <Aux>
            <div className="soccer-content">
            <Table 
                title={"EPL Table"}
                contents={standings}
                headers={standingsHeaders}
            />
            </div> 
            <div className="soccer-content">
            <Table 
                title={"Top Scorers"}
                contents={leaders}
                headers={leaderHeaders}
            />
            </div> 
        </Aux>
     );
}
 
export default soccer;