import React from 'react';

import Aux from '../../../hoc/Auxiliary';
import Button from '../../../UI/Button/Button';

import '../Calendar.css'

// task = db.Column(db.String(80), nullable=False)
// description = db.Column(db.Text, nullable=True)
// target_date = db.Column(db.DateTime, nullable=True)
// recurring = db.Column(db.Boolean, 
//                    nullable=False,
//                    default=False)


const calendarModal = (props) => {
    return (
        <Aux>
        <div className="row">
            <h1>{props.date.toDateString()}</h1>       
        </div>
        <div className="row">
            {props.children}
        </div>
        <Button
            value={'add'}
            btnType={'addCalendar'}
            clicked={() => console.log("click")}>
                Add
        </Button>
        </Aux> 
     );
}
 
export default calendarModal;