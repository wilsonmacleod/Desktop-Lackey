import React from "react";
import dateFns from "date-fns";

import Header from './Components/CalendarHeader';
import Days from './Components/CalendarDays';
import Cells from './Components/CalendarCells';

import './Calendar.css';

class Calendar extends React.Component {
  state = {
    currentMonth: new Date(),
    selectedDate: new Date(),
    setCurrentMonth: new Date(),
    setSelectedDate: new Date()
  };

  onDateClickHandler = day => {
    this.setState({
      selectedDate: day
    });
  };

  nextMonthHandler = () => {
    this.setState({
      currentMonth: dateFns.addMonths(this.state.currentMonth, 1)
    });
  };

  prevMonthHandler = () => {
    this.setState({
      currentMonth: dateFns.subMonths(this.state.currentMonth, 1)
    });
  };

  currentMonth = () => {
    this.setState({
      currentMonth: this.state.setCurrentMonth,
      selectedDate: this.state.setSelectedDate
    });
  };

  render() {
    return (
          <main>
            
            <div className="calendar">
                <Header
                  //data
                  currentMonth={this.state.currentMonth}
                  //handlers
                  prevMonth={this.prevMonthHandler}
                  nextMonth={this.nextMonthHandler}
               /> 
                <Days 
                  currentMonth={this.state.currentMonth}
                />

                <Cells 
                  currentMonth={this.state.currentMonth}
                  selectedDate={this.state.selectedDate}
                  setCurrentMonth={this.state.setCurrentMonth}
                  //handlers
                  onDateClick={this.onDateClickHandler}
                />
            </div>
        </main>
    );
  }
}

export default Calendar;
