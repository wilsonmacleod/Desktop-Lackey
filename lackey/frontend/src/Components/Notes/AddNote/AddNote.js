import React from 'react';

import Button from '../../UI/Button/Button';

import '../Notes.css';

const addNote = (props) => {
    return ( 
        <Button
            btnType={'addNote'}
            clicked={props.addNote}
        ><i className="fa fa-plus-square fa-3x" aria-hidden="true"></i></Button>
     );
}
 
export default addNote;