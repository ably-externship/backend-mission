import React from 'react';
import { BrowserRouter, Routes, Redirect, Route } from 'react-router-dom';
import Login from './components/Login';
import ProductList from './components/ProductList';
import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>      
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />}></Route>
          <Route path="/product-list" element={<ProductList />}></Route>
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;
