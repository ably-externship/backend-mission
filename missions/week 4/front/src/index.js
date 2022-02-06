import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import reportWebVitals from './reportWebVitals';

import Header from './components/header';
import App from './App';
import SignIn from './components/login';
import Logout from './components/logout';
import Single from './components/single';
import Delete from './components/delete';



const routing = ( 
  <Router>
      <React.StrictMode>
        <Header />
        <Routes>
          <Route path="/" element={<App />}/>
          <Route path="/login" element={<SignIn />}/>
          <Route path="/logout" element={<Logout />}/>
          <Route path="/product/:id" element={<Single />}/>
          <Route path="/delete/:id" element={<Delete />}/>
        </Routes>
      </React.StrictMode>
  </Router>
);

ReactDOM.render(
  routing
  , document.getElementById('root'));


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();


// ReactDOM.render(
//   <React.StrictMode>
//     <Header />
//     <Login />
//     <App />
//   </React.StrictMode>
//   , document.getElementById('root'));

// ReactDOM.render(
//   <React.StrictMode>
//     <Header />
//     <BrowserRouter>
//       <SignIn />
//       <App />
//     </BrowserRouter>
//   </React.StrictMode>
//   , document.getElementById('root'));