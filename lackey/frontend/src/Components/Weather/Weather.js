import React, { Component } from 'react';

import Aux from '../hoc/Auxiliary';
import Search from './Search/Search';
import Dashboard from './Dashboard/Dashboard';

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
        const data = this.state.data;
        let dashboards = null;
        if(data !== "None"){
            dashboards = [];
            for(let key in data){
                let dash = <Dashboard
                            locName={key}
                            propsData={data[key]}
                        />
                dashboards.push(dash);
            };

        }
        return ( 
            <Aux>
                <Search
                    wForm={this.props.wForm}
                    searchResults={this.props.searchData}
                    // handlers
                    searchCityOnChangeHandler={this.props.searchCityOnChangeHandler}
                    searchSubmit={this.props.searchCitySubmitHandler}
                    addWeatherLocation={this.props.addWeatherLocation}
                    clearSearchResults={this.props.searchCitySubmitHandler}
                />
               {dashboards}
            </Aux>
         );
    }
}
 
export default Weather;

/*
{city: [
date:"2020-05-14"
humidity:68
icon_link:"https://www.metaweather.com/static/img/weather/s.svg"
max_temp:78.75
min_temp:72.17
predictability:73
weather_state_name:"Showers"
wind_speed:4.624611398891805
woied:"2423945"
], + 5
}

*/