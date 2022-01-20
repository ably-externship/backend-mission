import React from 'react';
import {Link} from 'react-router-dom';
import '../css/Header.css';

function Header(){

    return(
        <>
            <div className="header">
                <div className="header-nav">
                    <div className="header-nav-links">
                        <Link className="header-logo" to="/">Velog</Link>
                        <Link to="/login"><button className="header-btn">로그인</button></Link>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Header;