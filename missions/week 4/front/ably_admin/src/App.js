import { useState, useEffect } from 'react'; // 내장함수 사용
import ProductList from './components/product/list'
import { BrowserRouter as Router,Route, Routes } from 'react-router-dom';
// import {ReactDOM }from 'react-dom'
// import ProductSummary from './components/product/summary';
import logo from './logo.svg';
import './App.css';
import Login from './components/Login'
import Navbar from './components/navbar'




function App() {
  // state만의 장점 웹이 app처럼 동작하게 만들고 싶어서 
  // state 가 변경시 html이 자동으로 재렌더링

  const  [username,setUsername]  = useState()
  const [market,setMarket] = useState("")

  return (
    <div >
      <Navbar  market = {market}/>

     
      <Router>
        <Routes >
          <Route path="/" element={<Home />} />
          <Route path="/product/" element={<ProductList />} />
          <Route path="/login/" element={<Login  setUsername={setUsername} setMarket = {setMarket}/>} />
        </Routes>
      </Router>


    </div>


  )

}

function Home() {
  
  return (
    <div className = "grid place-items-center h-screen" >
      {localStorage.getItem("username") +"님 반갑습니다"}
    </div>
  )
}

// ReactDOM.render(<App />, document.getElementById("root"));
export default App;
