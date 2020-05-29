import React from 'react';

import Button from '../../UI/Button/Button';

const removeNote = (props) => {
    return ( 
        <Button 
            clicked={props.removeNoteFunc} 
            val={props.id}
            btnType={'deleteTask'}>
                X
        </Button>
     );
}
 
export default removeNote;