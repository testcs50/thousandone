import React from 'react';
import {Switch, Route} from 'react-router-dom';
import Header from '../components/Header';
import MainPage from '../pages/MainPage';
import Questions from '../pages/Questions';
import MyActivity from '../pages/MyActivity';

export default class Layout extends React.Component {
    render () {
        const navItems = [
            {href: '/', title: 'Главная'},
            {href: '/questions', title: 'Вопросы'},
            {href: '/myactivity', title: 'Моя активность'}
        ]
        return (
            <div>
                <Header navItems={navItems}/>
                <div>
                    <Switch>
                        <Route exact path="/" component={MainPage}/>
                        <Route exact path="/questions" component={Questions}/>
                        <Route exact path="/myactivity" component={MyActivity}/>
                    </Switch>
                </div>
            </div>
        )
    }
}
