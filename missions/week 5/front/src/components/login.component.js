import React from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();

  const API_URL = process.env.REACT_APP_API;
  const loginUrl = `${API_URL}/accounts/sellers/signin`;
  const [id, setId] = React.useState("");
  const [password, setPassword] = React.useState("");
  console.log({ id, password });

  const onhandleLogin = async () => {
    const response = await fetch(loginUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: id,
        password: password,
      }),
    }).then((res) => res.json());
    console.log({ response });
    if (response) {
      const token = response.token;
      if (token) {
        const access = token.access;
        const refresh = token.refresh;
        if (access) {
          window.localStorage.setItem("ablyTk", access);
          navigate("/products");
        }
      } else {
        alert("아이디와 비밀번호를 확인해주세요");
      }
    }
  };

  return (
    <div>
      <input
        placeholder="아이디"
        onChange={(e) => {
          const value = e.target.value;
          setId(value);
        }}
      />
      <input
        placeholder="비밀번호"
        type="password"
        onChange={(e) => {
          const value = e.target.value;
          setPassword(value);
        }}
      />
      <button onClick={onhandleLogin}>로그인</button>
    </div>
  );
};

export default Login;
