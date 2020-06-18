import React from 'react';

import Button from '../../UI/Button/Button';

import './WeatherSearchResult.css';

/// title, location_type, woeid
const weatherSearchResult = (props) => {
    return ( 
        <div className="result">
            <p className="name">{props.title}</p>
            <p className="locationType">{props.locationType}</p>
            <p>
            <Button
                val={[props.title, props.woeid]}
                clicked={props.addLocation}
                btnType={"addLoc"}>
                    <div><b>+</b></div>
            </Button>
            </p>
        </div>
     );
}
 
export default weatherSearchResult;