import React from 'react';

import Button from '../../../UI/Button/Button';
import AddTaskForm from '../../../Forms/AddTaskForm';

import '../Calendar.css'

const calendarModal = (props) => {
    let selectedDate = props.date;
    console.log(selectedDate);
    //props.taskList
    let taskList = null;
    let data = props.data;
    if(data.length > 0){
        let tasks = [];
        for(let x = 0; x < data.length; x++){
          if(Number(data[x]['target_date'].split(",")[1]) === Number(selectedDate.getDate())){
            tasks.push(data[x]);
          }
        };
        taskList = tasks.map(i => {
          return <div 
                    key={i.id} 
                    className="row task">
                        {i.task} <Button
                                       value={i.id}
                                       disabled={false}
                                       btnType={'deleteTask'}
                                       clicked={() => console.log('deleting task ' + i.d)} 
                                    >-</Button>
                </div>
        });
      }


    let btnConfig = {
        'value': 'add',
        'type': 'addCalendar',
        'clicked': props.modalView,
        'text': '+'
    }
    let display = '';
    if (props.view === 'list'){
        display = taskList;
    }else{
        display = 
            <AddTaskForm
                    //data 
                    cForm={props.cForm}
                    selectedDate={selectedDate.toDateString()}
                    //hanlder
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
                {display}
            </div>

        </div>
     );
}
 
export default calendarModal;