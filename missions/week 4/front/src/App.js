import React, { useEffect, useState } from 'react';
import './App.css';
import Products from './components/products';
import ProductLoadingComponent from './components/productLoading';
import axiosInstance from './axios';



function App() {
	const ProductLoading = ProductLoadingComponent(Products);
	const [appState, setAppState] = useState({
		loading: true,
		products: null,
	});

	useEffect(() => {
		axiosInstance.get('/seller/').then((res) => {
			const allProducts = res.data;
			console.log(res.data);
			setAppState({ loading: false, products: allProducts });
			console.log(res.data);
		});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>상품 목록</h1>
			<ProductLoading isLoading={appState.loading} products={appState.products} />
		</div>
	);
}

export default App;