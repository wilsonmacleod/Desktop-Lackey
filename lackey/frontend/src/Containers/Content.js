import React, { Component } from 'react';

import Calendar from '../Components/Content/Calendar/Calendar';

import GET from '../axios/GET';
import POST from '../axios/POST';

const get = new GET()
const post = new POST()

class Content extends Component {
    state = { 
        view: 'Calendar',
        pullData: '',
        forms: {
            calendar: {
                name: '',
                description: '',
                targetDate: '',
                recurring: false
            }
        }
    }

/*    updateData = (type) => {    ///// DOES NOT FORCE RERENDER
        const pullType = {
            'Calendar': get.calendar()
        };
        let self = this;
        pullType[type]
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
                pullData: msg
            });
        });
    } */

    componentDidMount = () => {
        let viewContent = this.props.viewContent;
        let self = this;
        get.calendar()
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
                view: viewContent,
                pullData: msg
            });
        });
    }

    componentDidUpdate(prevProps){
        if(this.props.viewContent !== prevProps.viewContent){
            let viewContent = this.props.viewContent;
            this.setState({
                view: viewContent
            })
        }
    }

    formUpdateHandler = (event) => { // calendarTask
        let newState = this.state.forms;
        let formValue = event.target.value;
        let formName = event.target.name;
        let formField = event.target.getAttribute('id');
        const boolFields = ['recurring'];
        if(boolFields.includes(formField)){
            formValue = newState[formName][formField] ? false : true;
        };
        newState[formName][formField] = formValue;
        this.setState({
            forms: newState
        })
    }

    taskSubmitHandler = () => {
        const obj = JSON.stringify(this.state.forms.calendar);
        post.calendar(obj);
        this.updateData('Calendar')
    }

    render() { 
        console.log(this.state)
        let view = null;
        if(this.state.view === 'Calendar'){
            view = <Calendar 
                        cForm={this.state.forms.calendar} 
                        cFormHandler={this.formUpdateHandler}
                        taskSubmitHandler={this.taskSubmitHandler}
                    />
        }else{
            try {
                view = this.state.pullData[3]['task'] 
            }
            catch(err) {
                view = "null"
            }
    }
        return ( 
            <div>
            <div>{view}</div>
            </div>
         );
    }
}
 
export default Content;