import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Card from '../../UI/Card/Card';
import './Dashboard.css';

const dashboard = (props) => {
    let data = props.propsData;
    let cards = data.map(i => {
        return <Card
            cardType={'weatherDay'}
            header={
                <Aux>
                <img className="icon" src={i.icon_link} alt="" />
                </Aux>
            }   
        >
            {<p>{i.date}</p>}
            {<p>{i.weather_state_name}</p>}
        </Card>
    })
    return ( 
        <Aux>
            <h3 className="dash-title">{props.locName}</h3>
            <div className="dash-container">
                <div className="grid">
                    {cards}
                </div>
            </div>
        </Aux>
     );
}
 
export default dashboard;