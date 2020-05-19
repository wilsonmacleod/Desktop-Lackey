import React, { Component } from 'react';

import Aux from '../hoc/Auxiliary';
import Search from '../UI/Search/Search';
import Modal from '../UI/Modal/Modal';
import InvestmentForm from './InvestmentForm/InvestmentForm';
import Dashboard from './FinanceDashboard/FinanceDashboard';
import SearchResult from './FinanceSearchResult/FinanceSearchResult';


class Finance extends Component {
    state = { 
        showModal: false,
        selected: ''
    }

    modalHandler = (t) => {
        let toggle = this.state.showModal ? false : true;
        let newSelected = this.state.selected === '' ? t.target.value : '';
        this.setState({
          showModal: toggle,
          selected: newSelected
        })
      }
    
    render() {
        const data = this.props.data;
        const searchData = this.props.searchData;
    
        let searchResult = searchData.length >= 1 ? searchData.map(i => {
            return <SearchResult
                        symbol={i.stock_symbol}
                        name={i.name}
                        type={i.type}
                        currency={this.props.currency}
                        addFund={this.props.addFund}
                    />
        }) : null; 
    
        let figs = null;
        if(data !== 'None' &&
        searchResult === null){
            figs = []
            let dataObj = data['data'];
            let transObj = data['transactions'];
            for(let key in dataObj){
                let ele = 
                <Dashboard
                    title={key}
                    data={dataObj[key]}
                    transactions={transObj[key]}
                    updated={dataObj[key][0]['entered_date']}
                    refreshFund={this.props.refreshFund}
                    removeFund={this.props.removeFund}
                    modalHandler={this.modalHandler}
                />
                figs.push(ele)
                }
        }     
        return ( 
            <Aux>
                <Modal 
                    modalClass={"modal"}
                    showModal={this.state.showModal}
                    modalHandler={this.modalHandler}>
                        <InvestmentForm 
                            inputFormState={this.props.inputFormState}
                            selectedFund={this.state.selected}
                            active={this.state.showModal}
                            //handlers
                            inputFormOnChange={this.props.inputFormOnChange}
                            inputFormSubmit={this.props.inputFormSubmit}
                        />
                </Modal>
                <Search
                    searchFormState={this.props.searchFormState}
                    searchResult={searchResult}
                    //handlers
                    searchOnChange={this.props.searchOnChange}
                    searchSubmit={this.props.searchSubmit}
                    clearSearchResult={this.props.searchSubmit}
                />
                {figs}
        </Aux>
         );
    }
}

export default Finance;