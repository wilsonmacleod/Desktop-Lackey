import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Button from '../../UI/Button/Button';
import AddTaskForm from '../../Forms/AddTaskForm';

import '../Calendar.css'

const calendarModal = (props) => {
    let selectedDate = props.date;
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
            let desc = i.description !== "" ? 
            <li className="taskContainerLi"><b>Description: </b>{i.description}</li> : null;
            let time = i.time !== "" ?
             <li className="taskContainerLi"><b>Scheduled time: </b>{i.time}</li> : null;
            let recurring = i.recurring !== "False" ? 
            <li className="taskContainerLi">Scheduled to occur every {i.interval} days.</li> : null;

            return <Aux>
            <div className="taskContainer" key={i.id} >
            <Button
                        val={i.id}
                        disabled={false}
                        btnType={'deleteTask'}
                        clicked={props.taskDeleteHandler}
                        >
                        <i className="fa fa-minus fa-2x" aria-hidden="true"></i>
            </Button>
                    <div className="taskList">{i.task}</div> 
                    </div>
                    <ul>
                        {desc}
                        {time}
                        {recurring}
                    </ul>
                </Aux>
        });
      }

    let btnConfig = {
        'value': 'add',
        'type': 'addCalendar',
        'clicked': props.modalView,
        'text': <i className="fa fa-plus" aria-hidden="true"></i>
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
        btnConfig.text =  <i className="fa fa-eye" aria-hidden="true"></i>
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