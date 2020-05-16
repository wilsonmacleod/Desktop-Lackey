import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Card from '../../UI/Card/Card';
import Button from '../../UI/Button/Button';

import './Dashboard.css';

const dashboard = (props) => {
    let data = props.propsData;
    let cards = data.map(i => {
        let dateObject = new Date(i.date);
        let day = dateObject.toLocaleString('en-us', {  weekday: 'short' });
        let month = dateObject.toLocaleString('en-us', { month: 'short' });
        let date = dateObject.getDate();
        return <Card
                    cardType={'weatherDay'}
                    header={
                        <Aux>
                        <img className="icon" src={i.icon_link} alt="" />
                        <div className="date-title">{day} {month} {date}</div>
                        </Aux>
                    }>
                    <div className="centered">
                    <div className="data-title">{i.weather_state_name}</div>
                    <div className="text"><span className="data">{i.min_temp}</span>°F - <span className="data">{i.max_temp}</span>°F</div>
                    <div className="text">Humidity: <span className="data">{i.humidity}</span>%</div>
                    <div className="text">Wind Speed: <span className="data">{i.wind_speed.toFixed(2)}</span> MPH</div>
                    <div className="text">Predictability: <span className="data">{i.predictability}</span>%</div>
                    </div>
                </Card>
    })
    console.log(props.removeConfig)
    return ( 
        <Aux>
            <h3 className="dash-title">{props.locName}</h3>
            <div className="dash-container">
                <div className="grid">
                    {cards}
                </div>
            </div>
            <span className="text">Last Updated: {props.updated}</span>
            <Button btnType={"submit"} clicked={props.refreshForecast} val={props.locName}>Refresh</Button>
            <Button btnType={"remove"} clicked={props.removeConfig} val={props.locName}>Remove</Button>
        </Aux>
     );
}
 
export default dashboard;