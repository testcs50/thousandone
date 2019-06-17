import React from 'react';
import {Link} from 'react-router-dom';

export default class MenuItem extends React.Component {
    render () {
        return <li><Link to={this.props.navItem}>{this.props.children}</Link></li>
    }
}