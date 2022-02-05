import React, { useState } from "react";
import Axios from "axios";
import { useNavigate } from "react-router-dom";
import { useAppContext, setToken } from "../../store";

const LOGIN_API = "http://127.0.0.1:8000/api/token/";

const Login = () => {
  let navigate = useNavigate();
  const { dispatch } = useAppContext();
  const [inputs, setInputs] = useState({});

  const onSubmit = (e) => {
    e.preventDefault();
    async function fn() {
      try {
        const response = await Axios.post(LOGIN_API, inputs);
        const {
          data: { access: jwtToken },
        } = response;

        dispatch(setToken(jwtToken));
        navigate("/");
      } catch (error) {
        if (error.response) {
          alert("계정 정보를 확인해주세요.");
        }
      }
    }

    fn();
  };
  const onChange = (e) => {
    const { id, value } = e.target;
    setInputs((prev) => ({
      ...prev,
      [id]: value,
    }));
  };

  return (
    <div className="my-16 flex bg-gray-bg1">
      <div className="w-full max-w-md m-auto bg-white rounded-lg border border-primaryBorder shadow-default py-10 px-16">
        <h1 className="text-2xl font-medium text-primary mt-4 mb-12 text-center">
          관리자 전용 로그인 🔐
        </h1>

        <form onSubmit={onSubmit}>
          <div>
            <label htmlFor="email">Email</label>
            <input
              type="email"
              className={`w-full p-2 text-primary border rounded-md outline-none text-sm transition duration-150 ease-in-out mb-4`}
              id="email"
              placeholder="Your Email"
              onChange={onChange}
            />
          </div>
          <div>
            <label htmlFor="password">Password</label>
            <input
              type="password"
              className={`w-full p-2 text-primary border rounded-md outline-none text-sm transition duration-150 ease-in-out mb-4`}
              id="password"
              placeholder="Your Password"
              onChange={onChange}
            />
          </div>

          <div className="flex justify-center items-center mt-6">
            <button
              className={
                "bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
              }
            >
              로그인
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
