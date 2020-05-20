import React from 'react';

import Aux from '../hoc/Auxiliary';

const sports = (props) => {
    const data = props.data;
    console.log(data);
    return ( 
        <Aux>
            <h1>spurts</h1>
        </Aux>

     );
}
 
export default sports;


//NBA - scoreboard, standings, leaders (toggleable)
// EPL - "scoreboard"/fixtures, standings, scoring leaders
//NFL - scoreboard