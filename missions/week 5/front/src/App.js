import React, {useState, useEffect} from 'react';
import './App.css';
import Header from './components/Header/Header';
import CartPage from './components/Header/CartPage';
import LoginModal from './components/LoginModal';
import { Route } from 'react-router-dom';
import Product from "./components/Product";
import ProductRegister from "./components/Header/ProductRegister.js"
import ProductDetailPage from "./components/Product/ProductDetailPage";

function App() {
    const [modal, setModal] = useState(false);
    const [user, setUser] = useState([])
    const [loginedUserInfo ,setLoginedUserInfo] =  useState()


    let [isAuthenticated, setisAuthenticated] = useState(localStorage.getItem('token') ? true : false)


    // 토큰에서 페이로드(데이터) 부분 가져오기
    function getPayloadFromJWT(token) {
        const base64Payload = token.split(".")[1];
        return JSON.parse(atob(base64Payload));
    }

    //회원가입이나 로그인이 성공했을 때 토큰을 저장
    const userHasAuthenticated = (authenticated, username, token) => {
        setisAuthenticated(authenticated)
        setUser(username)
        // console.log(token)
        localStorage.setItem('token', token['access']);
        sessionStorage.setItem('token', token['refresh']);


        const userInfo = getPayloadFromJWT(token['access']);
        userInfo.accessToken = token['access']; // 이 토큰과
        userInfo.refreshToken = token['refresh'];
        setLoginedUserInfo(userInfo);
        // console.log(userInfo);
        // console.log(loginedUserInfo["user_id"]);
    }

    // 로그아웃
    const handleLogout = () => {
        setisAuthenticated(false);
        setUser('');
        localStorage.removeItem('token');
        setModal(false);
    };


    // console.log(isAuthenticated)
    
    // 회원가입이나 로그인이 성공했을 때 modal을 변경해 로그인 버튼을 없애고 글쓰기 버튼과 정보버튼을 나오게하는 setModal
    // useEffect의 두번째 인자는 모든 렌더링 후 두번째 인자가 변경될때에만 실행되라는 내용
    useEffect(()=>{
        if (isAuthenticated) {
            setModal(true);
        } else {
            setModal(false);
        }
    }, [isAuthenticated]);






    return (
        <>
            <div className="App">



                <div className="auto-margin">
                    <Header modal={modal} handleLogout={handleLogout}/>
                    <Route exact path="/">
                        <Product user={user}/>
                    </Route>
                    <Route path="/product/:id" component={ProductDetailPage}/>

                    {/*<Route path="/write">*/}
                    {/*    <ProductRegister user={user} loginedUserInfo={loginedUserInfo}/>*/}
                    {/*</Route>*/}
                    <Route path="/cart" component={CartPage}/>

                    <Route path="/login">
                        <LoginModal setModal={setModal} userHasAuthenticated={userHasAuthenticated}/>
                    </Route>
                </div>


            </div>
        </>
    );
}

export default App;