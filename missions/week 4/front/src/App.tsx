import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Login from "./components/Login";
import ProductList from "./components/ProductList";

function App() {
    const [tab, setTab] = useState<number>(0);

    const tabs = [
        (<div className="container"><Login/></div>), (<div className="container-fluid"><ProductList/></div>)
    ]

    const selectLoginTab = () => {
        setTab(0);
    }
    const selectProductListTab = () => {
        setTab(1);
    }

    return (
        <div className="App">
            <header>
                <div className="container">
                    <h3>M B L Y 관리자</h3>
                </div>
            </header>
            <hr/>
            <nav>
                <div className="container">
                    <ul className="nav nav-tabs">
                        <li className="nav-item">
                            <span className="nav-link" onClick={selectLoginTab}>로그인</span>
                        </li>
                        <li className="nav-item">
                            <span className="nav-link" onClick={selectProductListTab}>상품 목록</span>
                        </li>
                    </ul>
                </div>
            </nav>
            <section>
                {tabs[tab]}
            </section>
        </div>
    );
}

export default App;
