import "./App.css";
import Login from "./components/login.component";
import Products from "./components/products.component";
import { Route } from "react-router-dom";
import React from "react";
import { Routes, useNavigate } from "react-router-dom";

function App() {
  const navigate = useNavigate();

  React.useEffect(() => {
    const ablyTk = window.localStorage.getItem("ablyTk");
    if (!ablyTk) {
      navigate("/login");
    } else {
      navigate("/products");
    }
  }, []);

  return (
    <Routes>
      <Route exact path="/" element={<h1>main!</h1>} />
      <Route exact path="/login" element={<Login />} />
      <Route exact path="/products" element={<Products />} />
    </Routes>
  );
}

export default App;
