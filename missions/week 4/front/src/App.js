import React from "react";
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import Nav from "./components/nav";
// import Login from "./components/login";
import Login from "./pages/accounts/Login";
import ProductList from "./components/productList";

export default function App() {
  return (
    <Router>
      <Nav />
      <Routes>
        <Route
          exact
          path="/"
          element={<h1 className="text-center">Home Page</h1>}
        />
        <Route exact path="login" element={<Login />} />
        <Route exact path="products" element={<ProductList />} />
      </Routes>
    </Router>
  );
}
