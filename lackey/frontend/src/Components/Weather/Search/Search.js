import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Card from '../../UI/Card/Card';
import SearchForm from '../../Forms/SearchForm';
import SearchResult from './SearchResult/SearchResult';

const search = (props) => {
    let results = props.searchResults;
    let resultEle = results.length >= 1 ? results.map(i => {
        return <SearchResult
                    title={i.title}
                    locationType={i.location_type}
                    woeid={i.woeid}
                />
    }) : null;
    return ( 
        <Card
            cardType={"weatherSearch"}
            header={
                <Aux>
                <SearchForm 
                    wForm={props.wForm}
                    searchCityOnChangeHandler={props.searchCityOnChangeHandler}
                    searchSubmit={props.searchSubmit}
                />
                </Aux>
        }>
         {resultEle}
        </Card>

     );
}
 
export default search;