import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import '../css/LoginModal.css';
import axios from 'axios';


function LoginModal(props) {
    let [JoinLoign, setJoinLogin] = useState('로그인');
    const history = useHistory();

    let [username, setUsername] = useState();
    let [userpassword, setUserPassword] = useState();

    const data = {username: username, password: userpassword};

    const handleNameChange = (e) => {
        setUsername(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setUserPassword(e.target.value);
    };


    return (
        <>
            <div className="login-container">
                <div className="login-box">
                    <div className="exit">
                        <button onClick={()=>{ history.goBack(); }}>
                            <svg stroke="currentColor" fill="currentColor" viewBox="0 0 24 24" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></svg>
                        </button>
                    </div>
                    <span>{JoinLoign}</span>
                    <form>
                        {
                            JoinLoign === '로그인'
                                ? (
                                    <>
                                        <input type="text" placeholder="아이디를 입력하세요" onChange={handleNameChange}/>
                                        <input type="password" placeholder="비밀번호를 입력하세요" id="password" onChange={handlePasswordChange}/>
                                        <button className="JoinLoign-button" onClick={(e)=>{
                                            e.preventDefault();
                                            axios.post('http://localhost:8000/user/token/', data, {headers: {
                                                    'Content-Type': 'application/json'
                                                }})
                                                .then(response => {
                                                    // user data와 token정보가 일치하면 로그인 성공
                                                    if (response.data) {
                                                        alert('로그인 성공');
                                                        props.userHasAuthenticated(true, data.username, response.data);
                                                        history.push('/');
                                                        props.setModal(true);
                                                    } else {
                                                        alert('아이디 또는 비밀번호를 확인해주세요.');
                                                    }
                                                });
                                            // .catch(error => alert(error));
                                        }}>{JoinLoign}</button>
                                    </>
                                )
                                : (
                                    <>
                                        <input type="text" placeholder="아이디를 입력하세요" onChange={handleNameChange}/>
                                        <input type="password" placeholder="비밀번호를 입력하세요" onChange={handlePasswordChange}/>
                                        <button className="JoinLoign-button" onClick={(e)=>{
                                            e.preventDefault();
                                            fetch('http://localhost:8000/user/', {
                                                method: 'POST',
                                                headers: {
                                                    'Content-Type': 'application/json'
                                                },
                                                body: JSON.stringify(data)
                                            }).then(res => res.json())
                                                .then(json => {
                                                    if (json.username && json.token) {
                                                        props.userHasAuthenticated(
                                                            true,
                                                            json.username,
                                                            json.token);
                                                        history.push('/');
                                                        props.setModal(true);
                                                    } else {
                                                        // alert('사용불가능한 아이디입니다.');
                                                    }
                                                });
                                            // .catch(error => alert(error));
                                        }}
                                        >{JoinLoign}</button>
                                    </>
                                )
                        }
                    </form>
                    {/*<div className="login-foot">*/}
                    {/*    {*/}
                    {/*        JoinLoign === '회원가입'*/}
                    {/*            ? (*/}
                    {/*                <>*/}
                    {/*                    <span>이미 회원이신가요  ?</span>*/}
                    {/*                    <div className="foot-link" onClick={(e)=>{*/}
                    {/*                        e.preventDefault();*/}
                    {/*                        setJoinLogin('로그인');*/}
                    {/*                    }}>로그인</div>*/}
                    {/*                </>*/}
                    {/*            )*/}
                    {/*            : (*/}
                    {/*                <>*/}
                    {/*                    <span>아직 회원이 아니신가요 ?</span>*/}
                    {/*                    <div className="foot-link" onClick={(e)=>{*/}
                    {/*                        e.preventDefault();*/}
                    {/*                        setJoinLogin('회원가입');*/}
                    {/*                    }}>회원가입</div>*/}
                    {/*                </>*/}
                    {/*            )*/}
                    {/*    }*/}
                    {/*</div>*/}
                </div>
            </div>
        </>
    );
}
export default LoginModal;
