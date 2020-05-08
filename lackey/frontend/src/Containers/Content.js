import React, { Component } from 'react';

import Calendar from '../Components/Content/Calendar/Calendar';

import GET from '../axios/GET';

const get = new GET()

class Content extends Component {
    state = { 
        view: 'Calendar',
        pullData: ''
    }

    componentDidMount = () => {
        let viewContent = this.props.viewContent;
        let self = this;
        get.calendar()
        .then((result) => {
            result = result.data
            let msg = "Offline Mode";
            if (result.status === 200){
                let r = result.text;
                msg = r['data'];
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

    render() { 
        console.log(this.state)
        let view = this.state.view === 'Calendar'? <Calendar /> : this.state.pullData;
        return ( 
            <div>
            <div>{view}</div>
            </div>
         );
    }
}
 
export default Content;