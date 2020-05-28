import React from 'react';

import '../Notes.css';

const noteField = (props) => {
    let formField = <input 
                    type="text-area" 
                    className="note-field"
                    value={props.content} />
    return ( 
        <div className="note-field">{props.content}</div>
     );
}
 
export default noteField;