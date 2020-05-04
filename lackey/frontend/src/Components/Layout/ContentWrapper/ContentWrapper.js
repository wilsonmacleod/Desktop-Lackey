import React from 'react';

import '../Layout.css';

const contentWrapper = (props) => {
    return ( 

        <section id="main-content">
        <section className="wrapper">
                {props.children}
        </section>
      </section>
     );
    }
 
export default contentWrapper;