import React, { Component } from 'react';

import Search from './Search/Search';

class Weather extends Component {
    state = { 
        data: ''
     }

     componentDidMount(){
         let data = this.props.data;
         this.setState({
             data: data
         })
    }

    render() { 
        //console.log(this.state.data);
        return ( 
            <Search
                wForm={this.props.wForm}
                searchResults={this.props.searchData}
                // handlers
                searchCityOnChangeHandler={this.props.searchCityOnChangeHandler}
                searchSubmit={this.props.searchCitySubmitHandler}
                addWeatherLocation={this.props.addWeatherLocation}
            />
         );
    }
}
 
export default Weather;