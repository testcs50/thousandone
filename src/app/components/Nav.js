import React from 'react';
import MenuItem from './MenuItem';

export default class Nav extends React.Component {
    render() {
        let navItems = this.props.navItems.map((item, index) => <MenuItem key={index} navItem={item.href}>{item.title}</MenuItem>)
        return (
            <ul>
                {navItems}
            </ul>
        )
    }
}