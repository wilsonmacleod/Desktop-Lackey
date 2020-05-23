import React from 'react'

import Aux from '../../hoc/Auxiliary';

import './Table.css'

const table = (props) => {
    let contents = props.contents;
    let headers = props.headers; // array 
    let tableHeader = headers.map((key, index) => {
        return <th key={index}>{key.toUpperCase()}</th>
    })
    return ( 
        <Aux>
            <div className="master">{props.title}</div>
        <table>
           <tbody>
               {tableHeader}
              {contents}
           </tbody>
        </table>
        </Aux>
     );
}
 
export default table;