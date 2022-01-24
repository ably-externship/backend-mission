import React from "react";
import useInputs from "../hooks/useInputs";
import {setBearer, token} from "../modules/client";

const Login = () => {
    const [inputs, onChange] = useInputs({
        username: '',
        password: ''
    });

    const {username, password} = inputs;

    const onClick = () => {
        token(username, password).then(response => {
            console.log(response.data);
            const {access, refresh} = response.data;
            setBearer(access);
            localStorage.setItem('access', access);
            if (refresh)
                localStorage.setItem('refresh', refresh);
            alert('로그인 성공');
        }).catch(error => {
            console.log(error);
            alert('로그인 실패')
        })
    };

    return (
        <div>
            <div className="mb-3">
                <label htmlFor="username">사용자 이름</label>
                <input id="username" name="username" className="form-control" type="text" value={username}
                       onChange={onChange}/>
            </div>
            <div className="mb-3">
                <label htmlFor="password">비밀번호</label>
                <input id="password" name="password" className="form-control" type="password" value={password}
                       onChange={onChange}/>
            </div>
            <button className="btn btn-primary" onClick={onClick}>로그인</button>
        </div>
    );
};

export default Login;