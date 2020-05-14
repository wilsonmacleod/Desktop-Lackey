import React from 'react';

import Card from '../../UI/Card/Card';
import SearchForm from '../../Forms/SearchForm';

const search = (props) => {
    let results = props.searchResults;
    let resultEle = results.length > 1 ? results.map(i => {
        return <h1>{i.title}</h1>
    }) : null;
    return ( 
        <Card
            cardType={'weatherSearch'}
            header={
                <SearchForm 
                    wForm={props.wForm}
                    searchCityOnChangeHandler={props.searchCityOnChangeHandler}
                    searchSubmit={props.searchSubmit}
                />
        }>
         {resultEle}
        </Card>

     );
}
 
export default search;