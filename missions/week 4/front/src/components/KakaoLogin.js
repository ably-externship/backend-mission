import { useHistory } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import axios from "axios";
import styled from 'styled-components';

function KakaoLogin(){
    const { Kakao } = window;

    let history = useHistory();

    const dispatch = useDispatch();
    
    const kakaoLogin = () => {
        Kakao.Auth.login({
            success: function(response) {
                axios.get('http://localhost:8000/accounts/login/kakao', 
                { headers : { Authorization : response.access_token } })
                .then((response)=>{
                    
                    if ( response !== null && !response.date !== null ) {
                        
                        localStorage.setItem('access_token', response.data.access_token);
                        localStorage.setItem('account_type', response.data.account_type);
                        dispatch({ type : 'login', payload : response.data.account_type });
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