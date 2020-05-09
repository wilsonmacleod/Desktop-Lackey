import React from "react";
import dateFns from "date-fns";

import Header from './Components/CalendarHeader';
import Days from './Components/CalendarDays';
import Cells from './Components/CalendarCells';
import Modal from '../../UI/Modal/Modal';
import CalendarModal from '../Calendar/Components/CalendarModal';

import './Calendar.css';

class Calendar extends React.Component {
  state = {
    showModal: false,
    modalView: 'list',
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

  modalHandler = () => {
    let toggle = this.state.showModal ? false : true;
    this.setState({
      showModal: toggle,
      modalView: 'list'
    })
  }

  modalViewHandler = () => {
    let toggle = this.state.modalView === 'list' ? 'form' : 'list';
    this.setState({
      modalView: toggle
    })
  }

  render() {
    return (
          <main>
            <Modal
                //data
                modalClass={"modal"}
                showModal={this.state.showModal}
                //handler
                modalHandler={this.modalHandler}>
                  <CalendarModal 
                    //data
                    date={this.state.selectedDate}
                    view={this.state.modalView}
                    cForm={this.props.cForm}
                    //handler
                    modalView={this.modalViewHandler}
                    cFormHandler={this.props.cFormHandler}
                    taskSubmitHandler={this.props.taskSubmitHandler}
                  >
                    List
                  </CalendarModal>
                </Modal>
            
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
                  modalHandler={this.modalHandler}
                />
            </div>
        </main>
    );
  }
}

export default Calendar;
