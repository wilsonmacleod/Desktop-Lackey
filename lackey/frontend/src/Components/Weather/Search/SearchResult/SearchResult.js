import React from 'react';

import Button from '../../../UI/Button/Button';

import './SearchResult.css';

/// title, location_type, woeid
const searchResult = (props) => {
    return ( 
        <div className="result">
            <p className="name">{props.title}</p>
            <p className="locationType">{props.locationType}</p>
            <p>
            <Button
                val={[props.title, props.woeid]}
                clicked={props.addLocation}
                btnType={"addLoc"}>
                    <i class="fa fa-plus" aria-hidden="true"></i>
            </Button>
            </p>
        </div>
     );
}
 
export default searchResult;