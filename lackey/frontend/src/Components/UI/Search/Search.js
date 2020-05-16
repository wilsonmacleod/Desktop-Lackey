import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Card from '../Card/Card';
import Button from '../Button/Button';
import SearchField from './SearchField/SearchField';
//import SearchResult from '../../Weather/WeatherSearch/WeatherResult/WeatherResult';

const search = (props) => {
    let searchResult = props.searchResult;
    let top = searchResult !== null ? 
        <Button btnType={'submit'} clicked={props.clearSearchResult}>Clear</Button> 
        :                
        <SearchField 
            name={'search'}
            id={'query'}
            val={props.searchFormState.query}
            // handlers
            changed={props.searchOnChange}
            searchSubmit={props.searchSubmit}
        />;
    return ( 
        <Card
            cardType={'search'}
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
