import { useState, useEffect } from 'react';

function Navbar(props) {
    const [isLogin,setisLogin] = useState(false)
    return (
        <div>

            <nav className="relative w-full flex flex-wrap items-center justify-between py-3 bg-gray-100 text-gray-500 hover:text-gray-700 focus:text-gray-700 shadow-lg">
                <ul className="flex px-6">
                    <li className="mr-6">
                        <a className="text-blue-500 hover:text-blue-800" href="/">{localStorage.getItem("marketname")}관리자</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-blue-500 hover:text-blue-800" href="/product">상품리스트</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-blue-500 hover:text-blue-800" href="/login">Login</a>
                    </li>
                    <li className="mr-6">
                        <a className="text-gray-400 cursor-not-allowed" href="#">Disabled</a>
                    </li>
                </ul>
            </nav>
        </div>
    )
}

export default Navbar;