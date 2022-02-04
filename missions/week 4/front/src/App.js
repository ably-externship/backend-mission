import { Switch, Route } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { useEffect } from 'react';
import './App.css';
import HomeNav from './components/Navbar.js';
import SignupPage from './components/SignupPage.js';
import ProductList from './components/ProductListPage.js';
import LoginPage from './components/LoginPage.js';
import KakaoLogin from './components/KakaoLogin.js';
import AdminProductList from './components/AdminProductList.js';
import ProductRegistration from './components/ProductRegistration.js';

function App() {

  const dispatch = useDispatch();

  useEffect(()=>{
    if (localStorage.getItem('access_token') && localStorage.getItem('account_type')) {
      dispatch({ type : 'login' , payload : localStorage.getItem('account_type') });
    }
  }, []);

  return (
    <div className="App">
      
      <HomeNav/>

      <Switch>

        <Route exact path="/">
          <div className="Jumbotron">
            <h1>2022 NEW ARRIVALS!</h1>
          </div>
        </Route>

        <Route exact path="/products/list">
          <ProductList/>
        </Route>

        <Route exact path="/accounts/signup">
          <SignupPage/>
          <KakaoLogin/>
        </Route>

        <Route exact path="/accounts/login">
          <LoginPage/>
          <KakaoLogin/>
        </Route>

        <Route exact path="/admin/products">
          <AdminProductList/>
        </Route>

        <Route exact path="/products/registration"> 
          <ProductRegistration/>
        </Route>

      </Switch>

      

    </div>
  );
}

export default App;
