import React from 'react';

import Button from '../../../UI/Button/Button';
import AddTaskForm from '../../../Forms/AddTaskForm';

import '../Calendar.css'

// task = db.Column(db.String(80), nullable=False)
// description = db.Column(db.Text, nullable=True)
// target_date = db.Column(db.DateTime, nullable=True)
// recurring = db.Column(db.Boolean, 
//                    nullable=False,
//                    default=False)


const calendarModal = (props) => {

    let btnConfig = {
        'value': 'add',
        'type': 'addCalendar',
        'clicked': props.modalView,
        'text': '+'
    }
    //props.taskList
    const taskList = ["item", "item", "item", "item", "item"];
    let list = []
    if (props.view === 'list'){
        let x = 0;
        taskList.forEach(i => list.push(<div key={x++} className="row">{i}</div>))
    }else{
        list = <AddTaskForm 
                    cForm={props.cForm}
                    cFormHandler={props.cFormHandler}
                    taskSubmit={props.taskSubmitHandler}
                />
        btnConfig.text = 'eye'
    }
    return (
        <div className="modalField">

            <div className="row">
                <h1 className="title">{props.date.toDateString()}</h1>    
                <Button
                value={btnConfig.value}
                btnType={btnConfig.type}
                clicked={btnConfig.clicked}>
                    {btnConfig.text}
            </Button>   
            </div>

            <div className="row">
                {list}
            </div>

        </div>
     );
}
 
export default calendarModal;