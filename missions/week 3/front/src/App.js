import React, { useEffect, useState } from 'react';
import './App.css';
import Products from './components/products';
import ProductLoadingConponent from './components/productLoading';
import axiosInstance from './axios';




function App() {
	const ProductLoading = ProductLoadingConponent(Products);
	const [appState, setAppState] = useState({
		loading: false,
		products: null,
	});

useEffect(() => {
	setAppState({ loading: true });
	const apiUrl = `http://127.0.0.1:8000/manager/`;
	fetch(apiUrl)
	.then((data) => data.json())
	.then((products) => {
	setAppState({ loading: false, products: products });
	});
	}, [setAppState]);	

	if (localStorage.getItem('access_token')== null) {
		return (
			<div className="App">
				<h1>상품 리스트</h1>
				<ProductLoading isLoading={appState.loading} />
			</div>
		);
	} else {
		return (
			<div className="App">
				<h1>상품 리스트</h1>
				<ProductLoading isLoading={appState.loading} products={appState.products} />
			</div>
		);
	}
	
}
export default App;