import React, {useState} from "react";
import {
    findAllProducts,
    ProductResponse,
    refreshToken,
    removeProduct,
    searchProducts,
    setBearer
} from "../modules/client";
import useInputs from "../hooks/useInputs";

const ProductList = () => {
    const [products, setProducts] = useState<ProductResponse[]>([]);

    const refresh = () => {
        const refresh = localStorage.getItem('refresh');
        if (refresh) {
            refreshToken(refresh).then(response => {
                console.log(response.data);
                const {access} = response.data;
                setBearer(access);
                localStorage.setItem('access', access);
            }).catch(error => {
                console.log(error);
            });
        }
    };

    const onClick = () => {
        const access = localStorage.getItem('access');
        if (access)
            setBearer(access);
        refresh();

        findAllProducts().then(response => {
            console.log(response.data);
            setProducts(response.data);
        }).catch(error => {
            console.log(error);
            alert('상품 리스트를 불러오지 못했습니다.');
        });
    };

    const onClickRemove = (productId: number) => {
        if (window.confirm(`상품 ${productId}을(를) 삭제할까요?`)) {
            removeProduct(productId).then(response => {
                console.log(response.data);
                onClick();
            }).catch(error => {
                console.log(error);
            })
        }
    };

    const [inputs, onChange] = useInputs({query: ''});
    const search = () => {
        refresh();
        searchProducts(inputs.query).then(response => {
            console.log(response.data);
            setProducts(response.data);
        }).catch(error => {
            console.log(error);
        });
    };

    return (
        <>
            <div className="d-flex">
                <button className="btn btn-primary" onClick={onClick}>상품 리스트 불러오기</button>
                <div className="ms-1">
                    <div className="input-group">
                        <input type="text" className="form-control" placeholder="상품 검색" name="query"
                               value={inputs.query}
                               onChange={onChange}/>
                        <button className="btn btn-outline-secondary" onClick={search}>🔍</button>
                    </div>
                </div>
            </div>
            <table className="table">
                <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">market</th>
                    <th scope="col">name</th>
                    <th scope="col">display_name</th>
                    <th scope="col">original_price</th>
                    <th scope="col">discounted_price</th>
                    <th scope="col">hidden</th>
                    <th scope="col">sold_out</th>
                    <th scope="col">category</th>
                    <th scope="col">review_count</th>
                    <th scope="col">review_point</th>
                    <th scope="col">created_at</th>
                    <th scope="col">updated_at</th>
                    <th scope="col">삭제</th>
                </tr>
                </thead>
                <tbody>
                {products.map(product => (
                    <tr key={product.id}>
                        <th scope="row">{product.id}</th>
                        <td>{product.market}</td>
                        <td>{product.name}</td>
                        <td>{product.display_name}</td>
                        <td>{product.original_price}</td>
                        <td>{product.discounted_price}</td>
                        <td>{product.hidden}</td>
                        <td>{product.sold_out}</td>
                        <td>{product.category}</td>
                        <td>{product.review_count}</td>
                        <td>{product.review_point}</td>
                        <td>{product.created_at}</td>
                        <td>{product.updated_at}</td>
                        <td>
                            <button className="btn" onClick={onClickRemove.bind(this, product.id)}>❌</button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>
        </>

    );
};

export default ProductList;