import React from 'react';
import dateFns from "date-fns";

import '../Calendar.css';

const calendarHeader = (props) => {
    const dateFormat = "MMMM YYYY"
    return (
      <div className="header row middle">
        <div className="col col-start">
          <span className="icon" onClick={props.prevMonth}>
            Backwards
          </span>
        </div>
        <div className="col col-center">
          <span>{dateFns.format(props.currentMonth, dateFormat)}</span>
        </div>
        <div className="col col-end" onClick={props.nextMonth}>
          <span className="icon">Forwards
          </span>
        </div>
      </div>
    );
}
 
export default calendarHeader;