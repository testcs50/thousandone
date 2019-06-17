import React from 'react';
import Nav from './Nav';

export default class Header extends React.Component {
    render() {
        return (
            <header>
                <Nav navItems={this.props.navItems}/>
            </header>
        )
    }
}