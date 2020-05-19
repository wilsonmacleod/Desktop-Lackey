import React from 'react';

import Button from '../../UI/Button/Button';

import './InvestmentForm.css';

const investmentForm = (props) => {
    
    let btnDis = 'disabledSubmit';
    let submit = null;
    if(props.inputFormState.shareCount !== '' &&
    props.inputFormState.pricePerShare !== '' &&
    props.inputFormState.date !== ''){
        btnDis = 'submit';
        submit = props.inputFormSubmit;
    };
    if(props.inputFormState.stockSymbol === '' && props.active){
        props.inputFormOnChange({
            target: {
                value: props.selectedFund,
                id: "stockSymbol",
                name: "finance"
            }
            });
    };
    return ( 
        <fieldset>
                <h3>{props.selectedFund}</h3>
                <label>
                    <span>Number of Shares:<span className="req">*</span></span>
                    <input 
                        type="number"
                        value={props.inputFormState.shareCount}
                        name="finance"
                        id="shareCount"
                        onChange={props.inputFormOnChange}
                    />
                </label>

                <label>
                    <span>Price per share:<span className="req">*</span></span>
                    <input 
                        type="number"
                        value={props.inputFormState.pricePerShare}
                        name="finance"
                        id="pricePerShare"
                        onChange={props.inputFormOnChange}
                    />
                </label>

                <label>
                    <span>Price per share:<span className="req">*</span></span>
                    <input 
                        type="date"
                        value={props.inputFormState.date}
                        name="finance"
                        id="date"
                        onChange={props.inputFormOnChange}
                    />
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
 
export default investmentForm;