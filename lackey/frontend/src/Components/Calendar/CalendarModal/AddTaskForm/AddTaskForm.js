import React from 'react';

import Button from '../../../UI/Button/Button';

import './AddTaskForm.css';

const addTaskForm = (props) => {

    let btnDis = 'disabledSubmit';
    let submit = null;
    if(props.cForm.name !== '' &&
    props.cForm.targetDate !== ''){
        btnDis = 'submit';
        submit = props.taskSubmit
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

    let selectStyle = {backgroundColor: `#${props.cForm.color}`}
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
            <span>Color-code: </span>

            <select 
                value={props.cForm.color}
                style={selectStyle}
                name="calendar"
                id="color"
                onChange={props.cFormHandler}>
                <option id="1" value="4ecdc4"></option>
                <option id="2" value="3CB371"></option>
                <option id="3" value="F08080"></option>
                <option id="4" value="9370DB"></option>
                <option id="5" value="C0C0C0"></option>
            </select>
            </label>

                    <label>
                    <Button
                        value={'addTask'}
                        disabled={btnDis}
                        btnType={btnDis}
                        clicked={submit}
                    >
                        Submit
                    </Button>
                    </label>
        </fieldset>
        
     );
}
 
export default addTaskForm;