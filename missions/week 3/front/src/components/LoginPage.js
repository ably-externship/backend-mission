import { useState } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';
import './LoginPage.css';
import KakaoLogin from './KakaoLogin.js';


function LoginPage(){

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const history = useHistory();

    const emailHandler = (e) => {
        setEmail(e.target.value)
    };
    const passwordHandler = (e) => {
        setPassword(e.target.value)
    };

    const onClickHandler = (e) => {
        e.preventDefault();

        axios.post("http://localhost:8000/accounts/login", 
        { email : email, password : password })
        .then((response)=>{
            localStorage.setItem('access_token', response.data.access_token);
            history.push('/');
            alert('로그인 성공!');
        })
        .catch((error)=>{
            console.log(error);
            alert('이메일 또는 비밀번호가 틀렸습니다.')
        })
    };

    return(
        <div className="login">
            <form>
                <div>
                    <input type="text" placeholder="Email" onChange={emailHandler}/>
                </div>
                <div>
                    <input type="password" placeholder="Password" onChange={passwordHandler}/>
                </div>
                <div>
                    <button onClick={onClickHandler}>Log In</button>
                </div>
            </form>
                <div>
                    <KakaoLogin/>
                </div>
        </div>
    )
}

export default LoginPage