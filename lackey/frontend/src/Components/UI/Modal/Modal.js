import React from 'react';

import Aux from '../../hoc/Auxiliary';
import Backdrop from './Backdrop/Backdrop';

import'./Modal.css';

const Modal = (props) => {
    return ( 
        <Aux>
        <Backdrop
            show={props.showModal}
            clicked={props.modalHandler}
        />
        <div className={props.modalClass}
                style={{
                    transform: props.showModal ? 'translateY(0)' : 'translateY(-100vh)',
                    opacity: props.showModal ? '1': '0'
                }}
                >
                    {props.children}
        </div>
    </Aux> 
     );
}

export default Modal;