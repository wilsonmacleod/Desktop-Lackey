import React from 'react';

import Button from '../UI/Button/Button';

import './Forms.css';

const addTaskForm = (props) => {

    let btnDis = true;
    if(props.cForm.name !== '' &&
    props.cForm.targetDate !== ''){
        btnDis = false;
    }

    const split = props.selectedDate.split(" "); // add selected date to form state
    const formattedDate = `${[split[1],split[2],split[3]]}`;
    if(props.cForm.targetDate !== formattedDate){
        props.cFormHandler({
            target: {
                value: formattedDate,
                id: "targetDate",
                name: "calendar"
            }
        });
    };

    return ( 
        <fieldset>

                <label>
                    <span>Task:<span className="req">*</span></span>
                    <input 
                        type="text"
                        value={props.cForm.name}
                        name="calendar"
                        id="name"
                        onChange={props.cFormHandler}
                    />
                </label>

                <label>
                    <span>Description:</span>
                    <textarea 
                        type="text"
                        value={props.cForm.description}
                        name="calendar"
                        id="description"
                        onChange={props.cFormHandler}
                    />
                </label>

                <label>
                    <span>Time:</span>
                    <input 
                        type="text"
                        value={props.cForm.time}
                        name="calendar"
                        id="time"
                        onChange={props.cFormHandler}
                    />
                </label>
            
                <label>
                <span>Recurring?</span>
                    <input 
                        type="checkbox"
                        value={props.cForm.recurring}
                        name="calendar"
                        id="recurring"
                        onChange={props.cFormHandler}
                    />
                </label>

                {props.cForm.recurring ? 
                <label>
                    <span>Interval (days):<span className="req">*</span></span>
                    <input
                        type="number"
                        value={props.cForm.reccuringInterval}
                        name="calendar"
                        id="interval"
                        defaultValue={7}
                        onChange={props.cFormHandler}
                    />
                    </label>   
                    : null  
            }
                <label>
                <Button
                    value={'addTask'}
                    disabled={btnDis}
                    btnType={'submit'}
                    clicked={props.taskSubmit}
                >
                    Submit
                </Button>
                </label>
        </fieldset>
        
     );
}
 
export default addTaskForm;