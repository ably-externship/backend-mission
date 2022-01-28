import './SignupPage.css';
import { useState } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

function SignupPage (){

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
    const [phone, setPhone] = useState('');
    const history = useHistory();

    const emailHandler = (e) => {
        setEmail(e.target.value)
    };
    const passwordHandler = (e) => {
        setPassword(e.target.value)
    };
    const nameHandler = (e) => {
        setName(e.target.value)
    };
    const phoneHandler = (e) => {
        setPhone(e.target.value)
    };

    const onClickHandler = (e) => {
        e.preventDefault();

        axios.post("http://localhost:8000/accounts/signup", {
            email : email,
            password : password,
            name : name,
            phone_number : phone
        })
        .then(()=>{
            alert('회원가입 완료');
            history.push("/accounts/login");
        })
        .catch((error)=>{
            if (error.response) {
                const message = error.response.data.message;
                if (message === 'Invalid Email') {
                    alert('유효하지 않은 이메일 형식입니다.');
                } else if (message === 'Invalid Password') {
                    alert('비밀번호는 8-12자를 입력해주세요.')
                } else if (message === 'Invalid Name') {
                    alert('이름이 올바르지 않습니다.')
                } else if (message === 'Invalid Phone Number') {
                    alert('휴대폰 번호는 숫자만 입력해주세요.')
                } else if (message === 'Email Already Exists') {
                    alert('이미 가입된 이메일입니다.')
                }
            }
        })
    }

    return(
        <div className="signup">
            <form>
                <div>
                    <input type="text" placeholder="Email" onChange={emailHandler}/>
                </div>
                <div>
                    <input type="password" placeholder="Password" onChange={passwordHandler}/>
                </div>
                <div>
                    <input type="text" placeholder="Name" onChange={nameHandler}/>
                </div>
                <div>
                    <input type="tel" placeholder="Phone Number" onChange={phoneHandler}/>
                </div>
                <div>
                    <button onClick={onClickHandler}>Creat Account</button>
                </div>
            </form>
        </div>
    )
}

export default SignupPage