import React from 'react';
import dateFns from "date-fns";

import Button from '../../UI/Button/Button';

import '../Calendar.css';

const calendarCells = (props) => {
    //data
    let data = props.data
    //days
    const staticCurrentMonth = props.staticCurrentMonth
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
        if(dateFns.compareDesc(staticCurrentMonth, day) === -1 &&
        !dateFns.isSameDay(day, staticCurrentMonth)){
          x = <span className="slash">X</span>;
        };
        let taskForDay = ''
        if(data.length > 0){
          let tasks = [];
          for(let x = 0; x < data.length; x++){
            if(Number(data[x]['target_date'].split(",")[1]) === Number(date)){
              tasks.push(data[x]);
            }
          };
          taskForDay = tasks.map(i => {
            return <div
                      className="cTask"
                      >{i.task}</div>
          });
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
            <div className="cTaskContainer">
            {taskForDay}
            </div>
              <Button
                btnType={'calendarBtn'}
                val={date}
                clicked={props.modalHandler}>
                  +/-
                </Button>
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