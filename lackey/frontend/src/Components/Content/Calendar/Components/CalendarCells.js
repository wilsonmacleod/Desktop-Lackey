import React from 'react';
import dateFns from "date-fns";

import '../Calendar.css';

const calendarCells = (props) => {
    //days
    const currentMonth = props.currentMonth;
    const selectedDate = props.selectedDate;
    const monthStart = dateFns.startOfMonth(currentMonth);
    const monthEnd = dateFns.endOfMonth(monthStart);
    const startDate = dateFns.startOfWeek(monthStart);
    const endDate = dateFns.endOfWeek(monthEnd);

    let rows = [];
    let days = [];
    let day = startDate;

    const dateFormat = "D";
    let date = "";

    while (day <= endDate) {
      for (let i = 0; i < 7; i++) {
        date = dateFns.format(day, dateFormat);
        const cloneDay = day;
        let x = null; // past days
        if(dateFns.compareDesc(props.setCurrentMonth, day) === -1 &&
        !dateFns.isSameDay(day, props.setCurrentMonth)){
          x = <span className="slash">X</span>;
        }
        days.push(
          <div
            className={`col cell ${
              !dateFns.isSameMonth(day, monthStart)
                ? "disabled"
                : dateFns.isSameDay(day, selectedDate) ? "selected" : ''
            }`}
            key={day}
            onClick={() => props.onDateClick(dateFns.parse(cloneDay))}
          >
            <span className="number">{date}</span>
            {x}
            <div>
            </div>
          </div>
        );
        day = dateFns.addDays(day, 1);
      }
      rows.push(
        <div className="row" key={day}>
          {days}
        </div>
      );
      days = [];
    }
    return <div className="body">{rows}</div>;
}
 
export default calendarCells;