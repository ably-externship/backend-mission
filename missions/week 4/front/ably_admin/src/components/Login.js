import { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
function Login(props) {
    const [inputId, setInputId] = useState('')
    const [inputPw, setInputPw] = useState('')
    const navigate = useNavigate();

    // input data 의 변화가 있을 때마다 value 값을 변경해서 useState 해준다
    const handleInputId = (e) => {
        setInputId(e.target.value)
    }

    const handleInputPw = (e) => {
        setInputPw(e.target.value)
    }

    // login 버튼 클릭 이벤트   
    const onClickLogin = async () => {

        await axios.post("http://localhost:8000/api/account/token", {
            username: inputId,
            password: inputPw
        })
        .then(response => {
            localStorage.setItem("ACCESS_TOKEN", response.data.access)
            localStorage.setItem("REFRESH_TOKEN", response.data.refresh)
                if (response.status ==401){
                    console.log("hi")
                    alert("다시 시도해보세요")
                }
            })

            await axios.get("http://localhost:8000/api/account/token/info", {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem("ACCESS_TOKEN")}`
                }
            })

                .then(response => {
                    localStorage.setItem("username", response.data.username)
                    localStorage.setItem("is_staff", response.data.is_staff)
                    localStorage.setItem("marketname", response.data.market.name)
                    props.setUsername(response.data.username)
                    console.log(response.data.username)
                    console.log(props.username)

                    props.setMarket(response.data.market.name)
                })

            navigate("/")
        






    }

    // 페이지 렌더링 후 가장 처음 호출되는 함수
    // useEffect(() => {

    //     // // axios.get('/user_inform/login')
    //     // .then(res => console.log(res))
    //     // .catch()
    // },
    //     // 페이지 호출 후 처음 한번만 호출될 수 있도록 [] 추가
    //     [])

    return (
        <div>
            <div className="px">
                <form className="place-items-center  bg-white shadow-md rounded px-20 pt-6 pb-8 mb-4">
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" for="username">
                            Ably id
                        </label>
                        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Username" onChange={handleInputId}></input>
                    </div>
                    <div className="mb-6">
                        <label className="block text-gray-700 text-sm font-bold mb-2" for="password">
                            Password
                        </label>
                        <input className="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" onChange={handleInputPw} placeholder="******************"></input>
                        <p className="text-red-500 text-xs italic">Please choose a password.</p>
                    </div>
                    <div className="flex items-center justify-between">
                        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" onClick={onClickLogin} type="button">
                            로그인
                        </button>
                        <a className="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800" href="#">
                            Forgot Password?
                        </a>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Login;