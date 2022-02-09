import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Root from "./pages"; // pages/index.js import
import { BrowserRouter } from "react-router-dom";
import "antd/dist/antd.css";

ReactDOM.render(
    <BrowserRouter>
    <Root />
    </BrowserRouter>,
    document.getElementById('root')
);



