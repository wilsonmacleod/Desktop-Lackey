import React from 'react';


import '../Layout.css'

const sidebar = (props) => {
    const config = props.config;
    let options = [];
    for( let x = 0; x < config.length; x++) {
        options.push(
        <li key={x} value={config[x]} >
          <div 
            value={config[x]} 
            onClick={props.clicked}
            className={props.active === config[x] ? 'active' : ''}
          >
              <i value={config[x]} className={`fa fa-${props.sideBarIcons[x]}`} aria-hidden="true"></i>
              <span value={config[x]}>{config[x]}</span>
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

