import React, { Component } from "react";
import MallJoinPage from "./MallJoinPage";
import CreateMallPage from "./CreateMallPage";
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from "react-router-dom"

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (<Router>
            <Routes>
                <Route path='/join' component={MallJoinPage} />
                <Route path='/create' component={CreateMallPage} />            
            </Routes>
        </Router>);
    }
};