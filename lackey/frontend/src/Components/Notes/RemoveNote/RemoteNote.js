import React from 'react';

import Button from '../../UI/Button/Button';

const removeNote = (props) => {
    return ( 
        <Button 
            clicked={props.removeNoteFunc} 
            val={props.id}
            btnType={'deleteTask'}>
                <i value={props.id} className="fa fa-minus" aria-hidden="true" />
        </Button>
     );
}
 
export default removeNote;