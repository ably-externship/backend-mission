import './SignupPage.css';
import KakaoLogin from './KakaoLogin';

function SignupPage (){

    return(
        <div className="signup">
            <form>
                <div>
                    <input type="text" placeholder="Email" />
                </div>
                <div>
                    <input type="password" placeholder="Password" />
                </div>
                <div>
                    <input type="text" placeholder="Name" />
                </div>
                <div>
                    <input type="tel" placeholder="Phone Number" />
                </div>
                <div>
                    <button>Creat Account</button>
                </div>
                <div>
                    <KakaoLogin/>
                </div>
            </form>
        </div>
    )
}

export default SignupPage