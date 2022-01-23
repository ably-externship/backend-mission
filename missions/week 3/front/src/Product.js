import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ProductCard from './components/ProductTemplate';


function Products() {
  const [products, setProducts] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        // 요청이 시작 할 때에는 error 와 users 를 초기화하고
        setError(null);
        setProducts(null);
        // loading 상태를 true 로 바꿉니다.
        setLoading(true);
        const response = await axios.get(
          'http://localhost:8000/api/product'
        );
        setProducts(response.data);
        
      } catch (e) {
        setError(e);
      }
      setLoading(false);
    };

    fetchProducts();
  }, []);

  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러가 발생했습니다</div>;
  if (!products) return <div>데이터가 없습니다</div>;
  return (
    <ul>
      {products.map(product => (     
            <ProductCard
                ProductID={product.id}
                ImageURL={product.main_image}
                ProductName={product.product_name}
                Price={product.product_price}
                Shop={product.shop_id}/>            
        ))}
    </ul>  
  );
}

export default Products;