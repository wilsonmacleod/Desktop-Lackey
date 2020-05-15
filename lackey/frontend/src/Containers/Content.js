import React, { Component } from 'react';

import Loading from '../Components/UI/Loading/Loading';
import Calendar from '../Components/Calendar/Calendar';
import Weather from '../Components/Weather/Weather';

import GET from '../axios/GET';
import POST from '../axios/POST';
import DEL from '../axios/DEL';

const get = new GET()
const post = new POST()
const del = new DEL()

class Content extends Component {
    state = { 
        loading: false,
        view: '',
        data: '',
        forms: {
            calendar: {
                name: '',
                description: '',
                targetDate: '',
                time: '',
                recurring: false,
                interval: 7,
                color: '4ecdc4'
            },
            weather: {
                searchedCity: ''
            }
        },
        searchReturns: {
            weather: ''
        }
    };

    updateData = (view) => {
        this.setState({loading: true});
        const self = this;
        let dataFunction = null;
        if(view === "Weather"){
            dataFunction = get.weather()
        }else{
            dataFunction = get.calendar()
        };
        dataFunction 
        .then((result) => {
            result = result.data
            let data = "None";
            if (result.status === 200){
                let r = result.text;
                data = r['data'].replace(/'/g, '"');
                if (data !== "None"){
                    data = JSON.parse(data);
                };
            };
            self.setState({
                loading: false,
                view: view,
                data: data,
                forms: {
                    calendar: {
                        name: '',
                        description: '',
                        targetDate: '',
                        time: '',
                        recurring: false,
                        interval: 7,
                        color: '4ecdc4'
                    },
                    weather: {
                        searchedCity: ''
                    }
                },
                searchReturns: {
                    weather: ''
                }
            });
        });
    }

    componentDidMount = () => {
        let viewContent = this.props.viewContent;
        this.updateData(viewContent);
    };

    componentDidUpdate(prevProps){
        if(this.props.viewContent !== prevProps.viewContent){
            let viewContent = this.props.viewContent;
            this.updateData(viewContent);
        }
    };

    formUpdateHandler = (event) => {
        let newState = this.state.forms; 
        let formValue = event.target.value; // field value
        let formName = event.target.name; // calendar, weather etc.
        let formField = ''
        try {formField = event.target.getAttribute('id');} // spec field name
        catch(err){formField = event.target['id'];}

        const boolFields = ['recurring'];
        if(boolFields.includes(formField)){
            formValue = newState[formName][formField] ? false : true;
        };
        newState[formName][formField] = formValue;
        this.setState({
            forms: newState
        })
    };

    formSubmitHandler = (event) => {
        const view = this.state.view;
        let func, obj = '';
        if(view === 'Calendar'){
            obj = JSON.stringify(this.state.forms.calendar);
            func = post.calendar(obj);
        }else if(view === 'Weather'){
            let vals = event.target.value.split(",")
            obj = JSON.stringify({
                'city': vals[0],
                'woied': vals[1]
            });
            func = post.weatherConfig(obj);
        }
        func.then(() => {
            this.updateData(this.state.view)
        });
    };

    searchSubmitHandler = () => {
        const view = this.state.view;
        let newSearchReturns = this.state.searchReturns;
        let formState = this.state.forms;
        let func, obj, key = '';
        if(view === 'Weather'){
            obj = formState.weather.searchedCity;
            func = get.weatherCitySearch(obj);
            key = 'weather';
        }
        if (func && obj && key) {
            this.setState({loading: true});
            let self = this;
            func.then((result) => {
                let r = result.data.text;
                console.log(r)
                let data = r['data'].replace(/'/g, '"');
                newSearchReturns[key] = JSON.parse(data);
                formState.weather.searchedCity = '';
                self.setState({
                    loading: false,
                    forms: formState,
                    searchReturns: newSearchReturns,
                })
            });
        } else {
            this.updateData(view); //if no search reset state
        }
    }

    deleteHandler = (t) => {
        let id = t.target.value;
        del.calendar(id)
        .then(() => {
            this.updateData(this.state.view)
        });
    };

    render() { 
        console.log(this.state);
        let view = null;
        const views = {
            'Calendar': <Calendar 
                            data={this.state.data}
                            cForm={this.state.forms.calendar} 
                            //handlers
                            cFormHandler={this.formUpdateHandler}
                            taskSubmitHandler={this.formSubmitHandler}
                            taskDeleteHandler={this.deleteHandler}
                        />,
            'Weather': <Weather 
                            data={this.state.data}
                            searchData={this.state.searchReturns.weather}
                            wForm={this.state.forms.weather}
                            // handlers
                            searchCityOnChangeHandler={this.formUpdateHandler}
                            searchCitySubmitHandler={this.searchSubmitHandler}
                            addWeatherLocation={this.formSubmitHandler}
                        />
                    }
        try{
            view = this.state.loading ? <Loading /> : views[this.state.view];
        }catch(err){
            console.log(err);
            view = <div>Null</div>;
        };
        return ( 
            <div>
            {view}
            </div>
         );
    }
}
 
export default Content;