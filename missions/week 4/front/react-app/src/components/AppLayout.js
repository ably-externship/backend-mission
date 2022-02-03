import React from "react";
import "./AppLayout.css";



function AppLayout({ children }){
    return (
        <div className="app">
            <div className="header">

            </div>
            { children }
            <div className="footer">

            </div>
        </div>
    );

}

export default AppLayout;