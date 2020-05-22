import React from 'react';

import Aux from '../../../hoc/Auxiliary';
import Table from '../../../UI/Table/Table';

import '../SportsDashboard.css';

const nba = (props) => {
    const data = props.data;
    let standingsHeaders = ['', 'Team', 'Record', 'Win%', 'Home', 'Road', 'L10'];
    let counter = 0;
    let eastStandings = data.standings.map(i => {
        let clinched = i.data.ClinchIndicator.trim() === '- x' ? '(x)' : null;
        if(i.conference === 'East'){
            counter++;
            return <tr key={i.rank}>
            <td>{counter}</td>
            <td>{/*i.team_city*/}{i.team_name} {clinched}</td>
            <td>{i.data.Record}</td>
            <td>{(Number(i.data.WinPCT) * 100).toFixed(2)}</td>
            <td>{i.data.HOME}</td>
            <td>{i.data.ROAD}</td>
            <td>{i.data.L10}</td>
        </tr>
        }
    });
    counter = 0;
    let westStandings = data.standings.map(i => {
        let clinched = i.data.ClinchIndicator.trim() === '- x' ? '(x)' : null;
        if(i.conference === 'West'){
            counter++;
            return <tr key={i.rank}>
            <td>{counter}</td>
            <td>{/*i.team_city*/}{i.team_name} {clinched}</td>
            <td>{i.data.Record}</td>
            <td>{(Number(i.data.WinPCT) * 100).toFixed(2)}</td>
            <td>{i.data.HOME}</td>
            <td>{i.data.ROAD}</td>
            <td>{i.data.L10}</td>
        </tr>
        }
    });
    let leadersHeaders = ['Player', 'PTS', 'FG %', '3P %', 'FT %' ]
    let leaders = data.leaders.map(i => {
        return <tr key={i.rank}>
            <td>{i.player}</td>
            <td>{i.stats.PTS}</td>
            <td>{(Number(i.stats.FG_PCT) * 100).toFixed(2)}</td>
            <td>{(Number(i.stats.FG3_PCT) * 100).toFixed(2)}</td>
            <td>{(Number(i.stats.FT_PCT) * 100).toFixed(2)}</td>
    </tr>
    })
    return ( 
        <Aux>
            <div className="nba-content">
            <Table 
                title={"East"}
                contents={eastStandings}
                headers={standingsHeaders}
            />
            </div> 
            <div className="nba-content">
            <Table 
                title={"West"}
                contents={westStandings}
                headers={standingsHeaders}
            />
            </div>
            <div className="nba-content-last">
            <Table 
                title={"Leading Scorers"}
                contents={leaders}
                headers={leadersHeaders}
            />
            </div>
        </Aux>
     );
}
 
export default nba;