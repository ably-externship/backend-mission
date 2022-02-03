import React from 'react';
import { BrowserRouter, Routes, Redirect, Route } from 'react-router-dom';
import Login from './components/Login';
import ProductList from './components/ProductList';



function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />}></Route>
        <Route path="/product-list" element={<ProductList />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
