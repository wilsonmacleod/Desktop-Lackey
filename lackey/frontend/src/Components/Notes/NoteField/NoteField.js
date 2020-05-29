import React, { Component } from 'react';

import Aux from '../../hoc/Auxiliary';

import '../Notes.css';

class noteField extends Component {
    state = { 
        selected: false,
    };
    
    selectedToggle = () => {
        let toggle = this.state.selected ? false : true;    
        if(toggle){
            let content = this.props.content;
            let id = this.props.id;
            let color = this.props.color;
            this.props.notesFormHandler({
                target: {
                    value: content,
                    id: 'text',
                    name: 'notes'
                }
            });
            this.props.notesFormHandler({
                target: {
                    value: id,
                    id: 'id',
                    name: 'notes'
                }
            });
            this.props.notesFormHandler({
                target: {
                    value: color,
                    id: 'color',
                    name: 'notes'
                }
            });
        };
        this.setState({
            selected: toggle
        });
        return true
    };
    
    addNote = () => {
        this.selectedToggle()
        this.props.addNote();
    }

    render() {
        let content = this.state.selected ? this.props.nForm.text : this.props.content;
        let selectStyle = this.state.selected ? {backgroundColor: `#${this.props.nForm.color}`} : {backgroundColor: `#${this.props.color}`};
        return ( 
            <Aux>
                <select 
                    className="note-color"
                    value={this.props.nForm.color}
                    style={selectStyle}
                    name="notes"
                    id="color"
                    onFocus={this.selectedToggle}
                    onBlur={this.addNote}
                    onChange={this.props.notesFormHandler}>
                <option id="1" value="F0E68C"></option>
                <option id="2" value="4ecdc4"></option>
                <option id="3" value="F08080"></option>
                <option id="4" value="9370DB"></option>
                <option id="5" value="3CB371"></option>
            </select>
                <textarea
                    id="text"
                    name="notes"
                    className="ta-field"
                    onFocus={this.selectedToggle}
                    onBlur={this.addNote}
                    onChange={this.props.notesFormHandler}
                    value={content} 
                /> 
            </Aux>
         );
    }
}
 
export default noteField;