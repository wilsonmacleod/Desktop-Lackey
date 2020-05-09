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

  filterDataBySelectedMonth = (data, currentMonth) => {
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    let monthStr = months[currentMonth.getMonth()]
    let year = String(currentMonth.getFullYear());

    if(data !== ''){
      data = data.filter(i => {
        return data = i['target_date'].split(",")[0] === monthStr && 
        i['target_date'].split(",")[2] === year
      });
    }
    return data
  }

  render() {
    const data = this.filterDataBySelectedMonth(this.props.data, this.state.currentMonth);
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
                      data={data}
                      date={this.state.selectedDate}
                      view={this.state.modalView}
                      cForm={this.props.cForm}
                      //handler
                      modalView={this.modalViewHandler}
                      cFormHandler={this.props.cFormHandler}
                      taskSubmitHandler={this.props.taskSubmitHandler}
                    >
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
                  data={data}
                  currentMonth={this.state.currentMonth}
                  selectedDate={this.state.selectedDate}
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
