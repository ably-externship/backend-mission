import React from "react";
import { Route } from "react-router-dom";
import AppLayout from "../components/AppLayout";
import Home from "./Home";
import AccountRoutes from "./accounts";
import Product from "./Product"
import MarketOwnerProduct from "./MarketOwnerProduct"

function Root() {
       return (
            <AppLayout>
               <Route exact path="/" component={Home}  />
               <Route exact path="/products" component={Product}  />
               <Route exact path="/marketownerproduct" component={MarketOwnerProduct}  />
               <Route path="/accounts" component={AccountRoutes} />

            </AppLayout>
            );
}

export default Root;