import React from 'react';

import Button from '../../../UI/Button/Button';

import './SearchForm.css';

const searchForm = (props) => {
    return (               
    <div className="search">
       <input 
            type="text" 
            className="search-term" 
            name="weather" 
            id="searchedCity"
            placeholder="Search..."
            value={props.wForm.searchedCity}
            onChange={props.searchCityOnChangeHandler} />
            <Button
                btnType={"search-btn"}
                clicked={props.searchSubmit}>
                 <i class="fa fa-search"></i> 
            </Button>  
    </div>
     );
}
 
export default searchForm;

// searchTerm
// searchButton