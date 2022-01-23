import React, {Component} from 'react';
import { render } from "react-dom";
import "./App.css";
import RestAPI from "./RestAPI.js";


export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
        <div>
        <RestAPI />
        </div>
        );
    }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv)