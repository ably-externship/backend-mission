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
// import 'bootstrap/dist/css/bootstrap.css';

import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from 'react-router-dom';

// 리액트 리코일(상태관리, 쉽게 말하면 전역변수 관리, 컴포넌트간 데이터 공유에 필요)
import {
    RecoilRoot,
    atom,
    useRecoilState,
    useRecoilValue,
    selector
} from "recoil";


ReactDOM.render(
  <React.StrictMode>
      <RecoilRoot>
          <BrowserRouter>
              <App />
          </BrowserRouter>
      </RecoilRoot>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
