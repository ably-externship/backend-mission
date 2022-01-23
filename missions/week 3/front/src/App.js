import React from 'react';
import { createGlobalStyle } from 'styled-components';
import Products from './Product';
import FrontTemplate from './components/FrontTemplate';

const GlobalStyle = createGlobalStyle`  
  body {
    background: #facae1;
    font-family: 'Gowun Dodum', sans-serif;
  }

  h1 {
    padding-top: 30px;
    padding-bottom: 10px;
    text-align: center;
    color: white;
    border-bottom: 2px solid white;
    font-family: 'Gowun Dodum', sans-serif;
  }
`;

function App() {
  return (
      <>
        <GlobalStyle />
        <h1>Mutbly Admin</h1>
        <FrontTemplate>
        <Products />          
         </FrontTemplate>
      </> 
    );
}

export default App;

//import logo from './logo.svg';
//import './App.css';
//
//function App() {
//  return (
//    <div className="App">
//      <header className="App-header">
//        <img src={logo} className="App-logo" alt="logo" />
//        <p>
//          Edit <code>src/App.js</code> and save to reload.
//        </p>
//        <a
//          className="App-link"
//          href="https://reactjs.org"
//          target="_blank"
//          rel="noopener noreferrer"
//        >
//          Learn React
//        </a>
//      </header>
//    </div>
//  );
//}
//
//export default App;
