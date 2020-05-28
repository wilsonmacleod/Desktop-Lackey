import React from 'react';

import Aux from '../hoc/Auxiliary';
import AddNote from './AddNote/AddNote';
import RemoveNote from './RemoveNote/RemoteNote';
import NoteField from './NoteField/NoteField';

const notes = (props) => {
    const data = props.data;
    let noteCards = null;
    if(data.length < 6){
        let diff = 6 - data.length;
        for(let x = 0; x < diff; x++){
            props.addNote()
        };
    }else{
        noteCards = data.map(i => {
            let color = {backgroundColor: `#${i.color}`}
            return <div className="notes" style={color}>
                            <RemoveNote 
                                id={i.id}
                                removeNoteFunc={props.removeNote}
                            />
                            <NoteField content={'none this is a none, there is none'}/>
                    </div>
        });
    };
    return ( 
        <Aux>
            <AddNote
                addNote={props.addNote}
            />
            {noteCards}
        </Aux>
     );
}
 
export default notes;