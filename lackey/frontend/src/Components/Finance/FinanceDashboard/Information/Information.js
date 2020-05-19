import React from 'react';

import Aux from '../../../hoc/Auxiliary';

import '../FinanceDashboard.css';

const information = (props) => {
    const data = props.data;
    const labels = ['Current Price', 'Previous Price', 'Past Price'];
    let labelIndex = 0;
    let info = [];
    for(let x = 0; x < data.length; x++){
        let change = data[x].change.split(',');
        let sign= change[0];
        let perc = change[1];
        let changeCss = sign === '+' ? "increase" : "decrease";
        let ele = <div className="info-container">
                        <p><u><strong>{labels[labelIndex]}</strong></u></p>
                        <p>{data[x].date}</p>
                        <p>Close: <strong>{data[x].close}</strong> <span className={changeCss}> {perc}{sign}</span>%</p>
                        {data[x].opening === data[x].close ? null : <p>Open: <strong>{data[x].opening}</strong></p>}
                        {data[x].high === data[x].close ? null : <p>High: <strong>{data[x].high}</strong></p>}
                        {data[x].low === data[x].close ? null : <p>Low: <strong>{data[x].close}</strong></p>}
                    </div>
            info.push(ele);
            labelIndex = labelIndex === 2 ? 2 : labelIndex += 1;
    }
    return ( 
        <Aux>
            {info}
        </Aux>
     );
}
 
export default information;