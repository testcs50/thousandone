import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter, HashRouter} from 'react-router-dom';
import {Provider} from 'react-redux';
import store from './app/store';
import Layout from './app/layouts/Layout';

ReactDOM.render(
    <HashRouter>
        <Provider store={store}>
            <Layout/>
        </Provider>
    </HashRouter>,
 document.querySelector('#root'));