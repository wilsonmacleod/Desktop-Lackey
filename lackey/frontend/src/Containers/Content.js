import React, { Component } from 'react';

const contentSwitch = {
    'Home': 'ALL',
    'Calendar': 'Calendar',
    'Finance': 'Finance',
    'Sports': 'Sports',
    'Games': 'Games',
    'Scripts': 'Scripts'
}

class Content extends Component {
    state = { 
        view: '',
        pullData: ''
    }

    async fetchFunc(){
        const response = await fetch('/api/Hello');
        let json = await response.json();
        return json
      }

    componentDidMount = () => {
        let viewContent = contentSwitch[this.props.viewContent];
        let self = this;
        this.fetchFunc()
        .then(function (result){
            console.log(result)
            let msg = "Offline Mode";
            if (result.status == 200){
                let r = result.text;
                msg = r['Hello'];
            }
            self.setState({
                view: viewContent,
                pullData: msg
            });
        });
    }

    componentDidUpdate(prevProps){
        if(this.props.viewContent !== prevProps.viewContent){
            let viewContent = contentSwitch[this.props.viewContent]
            this.setState({
                view: viewContent
            })
        }
    }

    render() { 
        return ( 
            <div>
            <div>{this.state.view}</div>
            <div>{this.state.pullData}</div>
            </div>
         );
    }
}
 
export default Content;