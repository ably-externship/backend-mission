import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import { createStore } from 'redux';

const auth = { isLogin : false, account_type : ''};

function reducer(state=auth, action){
  if (action.type === 'login'){

    const copy = { ...auth };
    copy.isLogin = true;
    copy.account_type = action.payload;

    return copy

  } else if (action.type === 'logout'){

    const copy = { ...auth };
    copy.isLogin = false;
    copy.account_type = '';

    return copy
    
  } else  {
    return state
  }
};

const store = createStore(reducer);

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <Provider store={store}>
        <App />
      </Provider>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
