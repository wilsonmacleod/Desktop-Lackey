import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Card from '../../UI/Card/Card';
import Button from '../../UI/Button/Button';
import SearchForm from './SearchForm/SearchForm';
import SearchResult from './SearchResult/SearchResult';

const search = (props) => {
    let results = props.searchResults;
    let searchResult = results.length >= 1 ? results.map(i => {
        return <SearchResult
                    title={i.title}
                    locationType={i.location_type}
                    woeid={i.woeid}
                    addLocation={props.addWeatherLocation}
                />
    }) : null;
    let top = searchResult !== null ? 
        <Button btnType={"submit"} clicked={props.clearSearchResults}>Clear</Button> 
        :                
        <SearchForm 
            wForm={props.wForm}
            searchCityOnChangeHandler={props.searchCityOnChangeHandler}
            searchSubmit={props.searchSubmit}
        />;
    return ( 
        <Card
            cardType={"weatherSearch"}
            header={
                <Aux>
                {top}
                </Aux>
        }>
         {searchResult}
        </Card>

     );
}
 
export default search;