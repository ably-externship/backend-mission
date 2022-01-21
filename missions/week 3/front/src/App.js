import React, {useState, useEffect} from 'react';
import './App.css';
import Header from './components/Header';
import LoginModal from './components/LoginModal';
import { Route } from 'react-router-dom';
import Board from "./components/Board";
import Writer from "./components/Writer"

function App() {
    const [modal, setModal] = useState(false);
    const [user, setUser] = useState([])

    let [isAuthenticated, setisAuthenticated] = useState(localStorage.getItem('token') ? true : false)

    const userHasAuthenticated = (authenticated, username, token) => {
        setisAuthenticated(authenticated)
        setUser(username)
        localStorage.setItem('token', token['access']);
        sessionStorage.setItem('token', token['refresh']);
    }//회원가입이나 로그인이 성공했을 때 토큰을 저장

    const handleLogout = () => {
        setisAuthenticated(false);
        setUser('');
        localStorage.removeItem('token');
        setModal(false);
    };// 로그아웃

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

    console.log(user)

    return (
        <>
            <div className="App">
                <div className="auto-margin">

                    <Route exact path="/">
                        <Header modal={modal} handleLogout={handleLogout}/>
                        <Board user={user} />
                    </Route>

                    <Route exact path="/write">
                        <Writer user={user}/>
                    </Route>

                    <Route exact path="/login">
                        <LoginModal setModal={setModal} userHasAuthenticated={userHasAuthenticated}/>
                    </Route>

                </div>
            </div>
        </>
    );
}

export default App;