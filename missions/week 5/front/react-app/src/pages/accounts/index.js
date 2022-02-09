import React from "react";
import {Route} from "react-router-dom";
import Login from "./Login";


function Routes() {
    return (
        <>
            <Route exact path="/accounts/login" component={Login} />
        </>
    )
}

export default Routes;