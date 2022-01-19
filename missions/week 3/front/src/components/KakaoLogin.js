import { useHistory } from 'react-router-dom';
import axios from "axios";
import styled from 'styled-components';

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
            <KakaoImage src="/kakao_login.png" onClick={kakaoLogin}/>
        </div>
    )
}

const KakaoImage = styled.img`
    cursor: pointer;
    margin: 10px;`

export default KakaoLogin