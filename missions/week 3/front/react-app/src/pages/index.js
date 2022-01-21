import React from "react";
import { Route } from "react-router-dom";
import AppLayout from "../components/AppLayout";
import About from "./About";
import Home from "./Home";
import AccountRoutes from "./accounts";
import Product from "./Product"

function Root() {
       return (
            <AppLayout>
               <Route exact path="/" component={Home}  />
               <Route exact path="/product" component={Product}  />
               <Route path="/accounts" component={AccountRoutes} />

            </AppLayout>
            );
}

export default Root;