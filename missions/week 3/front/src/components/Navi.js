import React, { useState } from 'react';
import {Link} from 'react-router-dom';
import '../css/Navi.css';
import { Route } from 'react-router-dom';

function Navi(){
    let [underline, setUnderline] = useState({left:"0%"})

    return(
        <>
            <div className="navi-container">
                <div className="navi-box">
                    <Link className="navi-" to="/" onClick={()=>{
                        setUnderline({left:"0%"})
                    }}>
                        <span role = "img" aria-label = "하트">🤞최신</span>
                    </Link>
                    <Link className="navi-" to="/" onClick={()=>{
                        setUnderline({left:"50%"})
                    }}>
                        <span role = "img" aria-label = "질문">🤷‍♂️Q & A</span>
                    </Link>
                    <div className="navi-underline" style={underline}></div>
                </div>
            </div>
        </>
    )
}
export default Navi;