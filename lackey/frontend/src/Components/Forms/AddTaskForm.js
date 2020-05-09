import React from 'react';

import Button from '../UI/Button/Button';

import './Forms.css';

const addTaskForm = (props) => {
    let btnDis = true;
    if(props.cForm.name !== '' &&
    props.cForm.targetDate !== ''){
        btnDis = false;
    }
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
                    <span>Date:<span className="req">*</span></span>
                    <input 
                        type="datetime-local"
                        value={props.cForm.targetDate}
                        name="calendar"
                        id="targetDate"
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
                <div>
                <Button
                    value={'addTask'}
                    disabled={btnDis}
                    btnType={'submit'}
                    clicked={props.taskSubmit}
                >
                    Submit
                </Button>
                </div>

        </fieldset>
        
     );
}
 
export default addTaskForm;