import React from 'react';

import Aux from '../hoc/Auxiliary';
import AddNote from './AddNote/AddNote';
import RemoveNote from './RemoveNote/RemoveNote';
import NoteField from './NoteField/NoteField';

const notes = (props) => {
    const data = props.data;
    let noteCards = data.length <= 0 ? null :
    data.map(i => {
            let color = {backgroundColor: `#${i.color}`}
            let content = i.text.replace('|n', '\n');
            return <div className="notes" style={color}>
                            <RemoveNote 
                                id={i.id}
                                removeNoteFunc={props.removeNote}
                            />
                            <NoteField
                                id={i.id}
                                content={content}
                                color={i.color}
                                nForm={props.nForm}
                                //handlers
                                notesFormHandler={props.notesFormHandler}
                                addNote={props.addNote}
                            />
                    </div>
        });
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