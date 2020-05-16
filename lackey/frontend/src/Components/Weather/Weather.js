import React from 'react';

import Aux from '../hoc/Auxiliary';
import Search from '../UI/Search/Search';
import Dashboard from './Dashboard/Dashboard';
import SearchResult from './WeatherSearchResult/WeatherSearchResult';

const weather = (props) => {
    const data = props.data;
    const searchData = props.searchData;

    let searchResult = searchData.length >= 1 ? searchData.map(i => {
        return <SearchResult
                    title={i.title}
                    locationType={i.location_type}
                    woeid={i.woeid}
                    addLocation={props.addLocation}
                />
    }) : null;

    let dashboards = null;
    if(data !== "None" &&
    searchResult === null){
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
                searchFormState={props.searchFormState}
                searchResult={searchResult}
                // handlers
                searchOnChange={props.searchOnChange}
                searchSubmit={props.searchSubmit}
                clearSearchResult={props.searchSubmit}
            />
        {dashboards}
        </Aux>
     );
}
 
export default weather;
