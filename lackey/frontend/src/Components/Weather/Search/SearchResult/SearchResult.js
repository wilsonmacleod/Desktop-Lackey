import React from 'react';

import './SearchResult.css';

/// title, location_type, woeid
const searchResult = (props) => {
    return ( 
        <div className="result">
            <h5>{props.title}</h5>
            <p>{props.locationType}</p>
            <button>{props.woeid}</button>
        </div>
     );
}
 
export default searchResult;