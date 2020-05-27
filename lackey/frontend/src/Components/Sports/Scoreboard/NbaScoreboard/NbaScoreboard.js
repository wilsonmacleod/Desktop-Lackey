import React from 'react';

import Aux from '../../../hoc/Auxiliary';
import Table from '../../../UI/Table/Table';

import '../Scoreboard.css';

function cleanQuarters(data) {
    for(let each in data){
        try{
            let qs = data[each]['quarter_scores']
            let qtrs = qs.replace('{', '').replace('}', '').split(',');
            let qtrScore = {'total': 0};
            for(let x = 0; x < qtrs.length; x++){
                let qtr = Number(qtrs[x].split(':')[0].trim())
                let score = Number(qtrs[x].split(':')[1].trim())
                if(qtr <= 4 ){
                    qtrScore[String(qtr)] = score;
                }else if (score > 0){
                    qtrScore[String(qtr)] = score;
                }
                qtrScore['total'] += score
            };
            data[each]['quarter_scores'] =  qtrScore
        }catch(err){};
    }
    return data;
};

const nbaScoreboard = (props) => {
    const data = cleanQuarters(props.data);
    let gameIDs = [];
    let nba = data.map(i => {
        for(let x = 0; x < data.length; x++){
            let d = data[x];
            if(!gameIDs.includes(data[x].game_id) &&
                d.game_id === i.game_id && 
                d.team_abbr !== i.team_abbr){
                    gameIDs.push(i.game_id );
                    let game = [i,d];
                    let headers = [i.game_date, '1', '2', '3' , '4', ''];
                    let tableContents = game.map(g => {
                    return <tr key={g.game_id}>
                            <td className="team-name"><u>{g.team_city_name} {g.team_name}</u> ({g.record})</td>
                            <td className="team">{g.quarter_scores['1']}</td>
                            <td className="team">{g.quarter_scores['2']}</td>
                            <td className="team">{g.quarter_scores['3']}</td>
                            <td className="team">{g.quarter_scores['4']}</td>
                            <td className="total">{g.quarter_scores['total']}</td>
                        </tr>
                            });
                        return <Aux>
                                <div className="sbInfo">
                                        <Table
                                            headers={headers}  
                                            contents={tableContents}
                                        />
                                </div>
                            </Aux>
                    }
            }
        });
    if(data.length <= 0){
    nba = <div className="sbInfo">
            <Table
                headers={['No Games Today']}  
                contents={null}
            />
        </div>
    }
    return ( 
        <div className="scoreboard-container">
            {nba}
        </div>
     );
}
 
export default nbaScoreboard;