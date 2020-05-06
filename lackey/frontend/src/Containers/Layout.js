import React, { Component } from 'react';

import Aux from '../Components/hoc/Auxiliary';
import Header from '../Components/Layout/Header/Header';
import Sidebar from '../Components/Layout/Sidebar/Sidebar'; 
import ContentWrapper from '../Components/Layout/ContentWrapper/ContentWrapper';

class Layout extends Component {
    state = { 
        sideBarActive: 'Calendar',
        sideBarChoices: [
                        'Calendar', 
                        'Finance',
                        'Sports',
                        'Games',
                        'Scripts'
                        ]
      };

    sideBarClickHandler = (event) => {
        let clickedActive = event.target.getAttribute('id');
        this.setState({
            sideBarActive: clickedActive
            });
    }

    render() { 
        
        return ( 
            <Aux>
                <Header />
                <Sidebar 
                    active={this.state.sideBarActive}
                    config={this.state.sideBarChoices}
                    clicked={this.sideBarClickHandler}
                />
                <ContentWrapper>
                    {React.cloneElement(this.props.children, { viewContent: this.state.sideBarActive })}
                </ContentWrapper>

            </Aux>

         );
    }
}
 
export default Layout;