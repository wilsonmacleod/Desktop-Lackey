import React, { Component } from 'react';

import Loading from '../Components/UI/Loading/Loading';
import Calendar from '../Components/Content/Calendar/Calendar';

import GET from '../axios/GET';
import POST from '../axios/POST';

const get = new GET()
const post = new POST()

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
                recurring: false
            }
        },
        clearedForms: {
            calendar: {
                name: '',
                description: '',
                targetDate: '',
                time: '',
                recurring: false
            }
        },
    };

    updateData = (view) => {
        const clearedForms = this.state.clearedForms;
        const self = this;
        const updateCalls = {
            'Calendar': get.calendar()
        };
        updateCalls[view] 
        .then((result) => {
            result = result.data
            let msg = 'Offline Mode';
            if (result.status === 200){
                let r = result.text;
                msg = r['data'].replace(/'/g, '"');
                console.log(msg)
                msg = JSON.parse(msg);
            };  
            self.setState({
                loading: false,
                view: view,
                data: msg,
                forms: clearedForms
            });
        });
    };

    componentDidMount = () => {
        this.setState({loading: true})
        let viewContent = this.props.viewContent;
        this.updateData(viewContent);
    };

    componentDidUpdate(prevProps){
        if(this.props.viewContent !== prevProps.viewContent){
            let viewContent = this.props.viewContent;
            this.setState({
                view: viewContent
            })
        }
    };

    formUpdateHandler = (event) => { // calendarTask
        let newState = this.state.forms;
        let formValue = event.target.value;
        let formName = event.target.name;

        let formField = ''
        try {formField = event.target.getAttribute('id');} 
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

    taskSubmitHandler = () => {
        this.setState({loading: true})
        const obj = JSON.stringify(this.state.forms.calendar);
        post.calendar(obj)
        .then(() => {
            this.updateData('Calendar')
        });
    };

    render() { 
        console.log(this.state)
        let view = null;
        if(this.state.view === 'Calendar'){
            view = <Calendar 
                        data={this.state.data}
                        cForm={this.state.forms.calendar} 
                        //handlers
                        cFormHandler={this.formUpdateHandler}
                        taskSubmitHandler={this.taskSubmitHandler}
                    />
        }else{
            try {
                view = this.state.data[3]['task'] 
            }
            catch(err) {
                view = "null"
            }
    }
        view = this.state.loading ? <Loading /> : view;
        return ( 
            <div>
            {view}
            </div>
         );
    }
}
 
export default Content;