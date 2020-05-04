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
        pullData: {}
    }

    async fetchFunc(){
        const response = await fetch('/data');
        let json = await response.json();
        let results = json.text
        console.log(results)
        return results
      }


    componentDidMount = () => {
        let viewContent = contentSwitch[this.props.viewContent];
        let data = this.fetchFunc();
        this.setState({
            view: viewContent,
            pullData: data
        })
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
        console.log(this.state.pullData)
        return ( 
            <div>{this.state.view}</div>
         );
    }
}
 
export default Content;