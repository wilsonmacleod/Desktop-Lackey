import React, { Component } from 'react';

import Aux from '../Components/hoc/Auxiliary';
import Loading from '../Components/UI/Loading/Loading';
import Calendar from '../Components/Calendar/Calendar';
import Weather from '../Components/Weather/Weather';
import Finance from '../Components/Finance/Finance';

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
            search: {
                query: ''
            }
        },
        searchReturns: ''
    };

    updateData = (view) => {
        this.setState({loading: true});
        const self = this;
        get.init(view, 'init') 
        .then((result) => {
            result = result.data
            let data = 'None';
            if (result.status === 200){
                let r = result.text;
                data = r['data'].replace(/'/g, '"');
                if (data !== 'None'){
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
                    search: {
                        query: '',
                    }
                },
                searchReturns: ''
            });
        });
    };

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
        let obj = '';
        if(view === 'Calendar'){
            obj = JSON.stringify(this.state.forms.calendar);
        }else if(view === 'Weather'){
            let vals = event.target.value.split(',');
            obj = JSON.stringify({
                'city': vals[0],
                'woied': vals[1]
            });
        }else if(view === 'Finance'){
            let vals = event.target.value.split(',');
            obj = JSON.stringify({
                'stock_symbol': vals[0],
                'name': vals[1]
            });
        };
        post.add(view, obj).then(() => {
            this.updateData(view)
        });
    };

    searchSubmitHandler = () => {
        const view = this.state.view;
        let formState = this.state.forms;
        let obj = formState.search.query;
        if (obj !== '') {
            this.setState({loading: true});
            let newSearchReturns = this.state.searchReturns;
            let self = this;
            get.search(view, obj).then((result) => {
                let r = result.data.text;
                console.log(r)
                let data = r['data'].replace(/'/g, '"');
                newSearchReturns = JSON.parse(data);
                formState.search.query = '';
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
        const view = this.state.view;
        let id = t.target.value;
        del.delete(view, id).then(() => {
            this.updateData(view);
        });
    };
    
    forceRefreshDataHandler = (t) => {
        const view = this.state.view;
        const a = 'refresh';
        const id = t.target.value;
        const action = [`${a}=${id}`];
        get.init(view, action).then(() => {
            this.updateData(view);
        });
    }

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
                            searchData={this.state.searchReturns}
                            searchFormState={this.state.forms.search}
                            // handlers
                            searchOnChange={this.formUpdateHandler}
                            searchSubmit={this.searchSubmitHandler}
                            addLocation={this.formSubmitHandler}
                            removeConfig={this.deleteHandler}
                            refreshForecast={this.forceRefreshDataHandler}
                        />,
            'Finance': <Finance
                            data={this.state.data}
                            searchData={this.state.searchReturns}
                            searchFormState={this.state.forms.search}
                            //handlers
                            searchOnChange={this.formUpdateHandler}
                            searchSubmit={this.searchSubmitHandler}
                            addFund={this.formSubmitHandler}
                        />
                    };
        try{
            view = this.state.loading ? <Loading /> : views[this.state.view];
        }catch(err){
            console.log(err);
            view = <Aux>Null</Aux>;
        };
        return ( 
            <div>
                {view}
            </div>
         );
    }
}
 
export default Content;