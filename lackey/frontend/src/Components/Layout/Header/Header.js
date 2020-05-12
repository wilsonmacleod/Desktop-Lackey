import React from 'react';

import '../Layout.css';

const header = () => {
    return ( 
        <header className="header black-bg">
        <div className="logo"><b>LACKEY<span>WM</span></b></div>
        <div className="nav notify-row">   
          <div className="date">
              {new Date().toDateString()}
        </div>   
        </div>
        <div className="top-menu">
        </div>
        </header>
     );
}
 
export default header;