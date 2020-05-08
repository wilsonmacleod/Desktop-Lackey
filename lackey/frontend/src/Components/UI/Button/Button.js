import React from 'react';

import './Button.css';

const button = (props) => (
    <button
        value={props.val}
        disabled={props.disabled}
        className={props.btnType}
        onClick={props.clicked}>{props.children}</button>
);

export default button;