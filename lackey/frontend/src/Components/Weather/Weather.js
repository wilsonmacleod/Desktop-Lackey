import React from 'react';

import Aux from '../hoc/Auxiliary';
import Search from './Search/Search';
import Dashboard from './Dashboard/Dashboard';

const weather = (props) => {
    const data = props.data;
    const searchResults = props.searchData;
    let dashboards = null;
    if(data !== "None" &&
    searchResults === ''){
        dashboards = [];
        for(let key in data){
            let dash = <Dashboard
                            locName={key}
                            propsData={data[key]}
                            updated={data[key][0]['entered_date']}
                            // handlers
                            refreshForecast={props.refreshForecast}
                            removeConfig={props.removeConfig}
                        />
            dashboards.push(dash);
        }
    }
    return ( 
        <Aux>
            <Search
                wForm={props.wForm}
                searchResults={searchResults}
                // handlers
                searchCityOnChangeHandler={props.searchCityOnChangeHandler}
                searchSubmit={props.searchCitySubmitHandler}
                addWeatherLocation={props.addWeatherLocation}
                clearSearchResults={props.searchCitySubmitHandler}
            />
        {dashboards}
        </Aux>
     );
}
 
export default weather;
