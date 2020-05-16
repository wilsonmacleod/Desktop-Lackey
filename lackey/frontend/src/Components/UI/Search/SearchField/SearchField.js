import React from 'react';

import Button from '../../Button/Button';

import './SearchField.css';

const searchField = (props) => {
    return (               
    <div className="search">
       <input 
            type="text" 
            className="search-term" 
            name={props.name} 
            id={props.id}  
            placeholder="Search..."
            value={props.val} 
            onChange={props.changed} 
          />
          <Button
               btnType={"search-btn"}
               clicked={props.searchSubmit}>
               <i class="fa fa-search"></i> 
          </Button>  
    </div>
     );
}
 
export default searchField;
