import React,{useState,useEffect} from "react";
import {Link, useHistory} from 'react-router-dom';
import axios from "axios";

function Header(props){



    return(
        <>
            <div className="header">
                <div className="header-nav">
                    <div className="header-nav-links">



                        <Link className="header-logo" to="/">MBLY</Link>
                        {
                            props.modal === false
                            ?<Link to="/login"><div className="menu">로그인</div></Link>
                                :(
                                    <div className="writer-button-1">
                                        <ul className="row">
                                            {/*<li className="cell"><Link to="/write"><div className="menu">상품 등록</div></Link></li>*/}
                                            <li className="cell"><Link to="/cart"><div className="menu">장바구니</div></Link></li>
                                            <li className="cell"><Link onClick={props.handleLogout} to="/"><div className="menu">로그아웃</div></Link></li>
                                        </ul>
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