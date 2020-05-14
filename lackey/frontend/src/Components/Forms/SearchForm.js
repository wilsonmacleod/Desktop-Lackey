import React from 'react';

import Button from '../UI/Button/Button';

const searchForm = (props) => {
    return ( 
        <div className="wrap">
        <div className="search">
                <input 
                    type="text" 
                    className="search-term" 
                    name="weather"
                    id="searchedCity"
                    value={props.wForm.searchedCity}
                    onChange={props.searchCityOnChangeHandler}
                />
                <Button
                    clicked={props.searchSubmit}
                >
                <i className="fa fa-search"></i>
                    </Button>                 
        </div>
        </div>
     );
}
 
export default searchForm;
