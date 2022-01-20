// api.js
import axios from 'axios';
const API = axios.create();

// Developer
export const ProductList = () => API.get("/apis/product/"); // 개발자 리스트 출력
export const ProductDetail = ((id, name, price) => API.post("/apis/product/", {
    id: id,
    name: name,
    price: price
})); // 개발자 생성



//// api.js
//import axios from 'axios';
//import React, { Component } from 'react';
//import
//
//class App extends Component {
//    state = {
//        products: []
//    };
//
//    async componentDidMount() {
//        try {
//            const res await fetch('http://127.0.0.1:8000/apis/product/');
//            const products = await res.json();
//            this.setState({
//                products
//            });
//        } catch (e) {
//            console.log(e);
//        }
//    }
//
//    render() {
//        return (
//            <div>
//                {this.state.products.map(item => (
//                    <div key={item.id}>
//                        <h1>{item.name}</h1>
//                        <span>{item.price}
//                    </div>
//                ))}
//            </div>
//        );
//    }
//}
//
//export default App;
//
