import React from 'react';


import '../Layout.css'

const sidebar = (props) => {
    const config = props.config;
    let options = [];
    for( let x = 0; x < config.length; x++) {
        options.push(
        <li key={x}>
            <div 
              id={config[x]}
              className={props.active === config[x] ? 'active' : ''}
              onClick={props.clicked}
            >
                <i className="fa fa-dashboard"></i>
                <span>{config[x]}</span>
            </div>
        </li>
        )
    };

    return ( 
    <aside>
      <div id="sidebar" className="nav-collapse">
        <ul className="sidebar-menu" id="nav-accordion">
        {options}
        </ul>
      </div>
    </aside>
     );
}

export default sidebar;

