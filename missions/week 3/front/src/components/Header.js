import React from 'react';
import {Link} from 'react-router-dom';
import '../css/Header.css';

function Header(props){

    return(
        <>
            <div className="header">
                <div className="header-nav">
                    <div className="header-nav-links">
                        <Link className="header-logo" to="/">MBLY</Link>
                        {
                            props.modal === false
                            ?<Link to="/login"><button className="header-btn">로그인</button></Link>
                                :(
                                    <div>
                                        <Link className="header-dashboard" to="/write"><button>새 글 작성</button></Link>
                                        <Link onClick={props.handleLogout} to="/"><div className="menu">로그아웃</div></Link>
                                    </div>

                                )
                        }
                    </div>
                </div>
            </div>
        </>
    )
}

export default Header;