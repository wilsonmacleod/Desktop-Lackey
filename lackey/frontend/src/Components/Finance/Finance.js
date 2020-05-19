import React from 'react';

import Aux from '../hoc/Auxiliary';
import Search from '../UI/Search/Search';
import Dashboard from './FinanceDashboard/FinanceDashboard';
import SearchResult from './FinanceSearchResult/FinanceSearchResult';
import FinanceFigures from './FinanceFigures/FinanceFigures';

const finance = (props) => {
    const data = props.data;
    const searchData = props.searchData;

    let searchResult = searchData.length >= 1 ? searchData.map(i => {
        return <SearchResult
                    symbol={i.stock_symbol}
                    name={i.name}
                    type={i.type}
                    currency={props.currency}
                    addFund={props.addFund}
                />
    }) : null; 

    let figs = null;
    if(data !== 'None' &&
    searchResult === null){
        figs = []
        for(let key in data){
            let ele = 
            <Dashboard
                title={key}
                figure = {
                    <FinanceFigures 
                        data={data[key]}
                        key={key}
                    /> 
                }
                updated={data[key][0]['entered_date']}
                refreshFund={props.refreshFund}
                removeFund={props.removeFund}
            />
            figs.push(ele)
            }
    }

    return ( 
        <Aux>
            <Search
                searchFormState={props.searchFormState}
                searchResult={searchResult}
                //handlers
                searchOnChange={props.searchOnChange}
                searchSubmit={props.searchSubmit}
                clearSearchResult={props.searchSubmit}
            />
            {figs}
        </Aux>
     );
}
 
export default finance;