import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import axios from 'axios';
import { setCookie, getCookie } from '../cookie';

const LoginBlock = styled.div`
    margin: 0 auto;
`;

function LoginTemplate() {
    const [message, setMessage] = useState("");
    const [response, setResponse] = useState(null);

    const isUser = (e) => {
        e.preventDefault()
        alert(e.target.id.value);
        alert(e.target.password.value);
        const id = e.target.id.value;
        const password = e.target.password.value;

        const response = axios.post(
            'http://localhost:8000/api/token/', {
                username: `${id}`,
                password: `${password}`,
            }).then(response => {
                // response 
                setResponse(response.data);
                console.log(response.data.access);
                setCookie('access_token', response.data.access, {
                    path: "/",
                    secure: true,
                    sameSite: "none", 
                })

           }).catch(error => {
               alert(error);
           }).then(() => {
               // 항상 실행
           });
    }
    if (getCookie('access_token')){
        return `<p>있음</p>`
    }
    return (
        <LoginBlock>
            <form onSubmit={isUser}>
                <label>입점사 id</label>
                <input type='text' name='id'/>
                <label>비밀번호</label>
                <input type='password' name='password'/>
                <button className="btn btn-outline-danger" type='submit'>로그인</button>
                <p>{message}</p>
            </form>
        </LoginBlock>
    )

}

export default LoginTemplate;