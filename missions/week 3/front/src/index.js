import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import './assets/base.css';
import './assets/tailwind.css';
import './css/main.css';
import './css/Header.css';
import './css/LoginModal.css';
import './css/Product.css';
import './css/Sign.css';
import './css/Writer.css';

import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from 'react-router-dom';

ReactDOM.render(
  <React.StrictMode>
      <BrowserRouter>
          <App />
      </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
