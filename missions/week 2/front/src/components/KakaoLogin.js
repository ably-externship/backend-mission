import { useHistory } from 'react-router-dom';
import axios from "axios";

function KakaoLogin(){
    const { Kakao } = window;

    let history = useHistory();
    
    const kakaoLogin = () => {
        Kakao.Auth.login({
            success: function(response) {
                axios.get('http://localhost:8000/accounts/login/kakao', 
                { headers : { Authorization : response.access_token } })
                .then((response)=>{
                    if ( response.data.access_token ) {
                        localStorage.setItem('access_token', response.data.access_token);
                        history.push('/');
                    }
                });
            },
            fail: function(error) {
                console.log(error);
            }
        })
    }

    return(
        <div>
            <img src="/kakao_login.png" onClick={kakaoLogin}/>
        </div>
    )
}

export default KakaoLogin