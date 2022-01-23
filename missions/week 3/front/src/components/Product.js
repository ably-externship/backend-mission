import React,{useState, useEffect} from 'react';
import {Link, useHistory} from 'react-router-dom';
import axios from 'axios';

function Product(props) {

    const history = useHistory();

    const [productList, setProductList] = useState([]);

    useEffect(() => {
        const take = async () => {
            const {data} = await axios.get('http://127.0.0.1:8000/product/');
            setProductList(data);
        };
        take();
    }, []);

    const Deleteproduct = async (product_id)=> {
        if(!!localStorage.getItem('token')) {
            if (window.confirm('정말 삭제하시겠습니까 ?') === true) {
                await axios.delete('http://localhost:8000/product/delete/' + product_id + '/', {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`,
                    }
                }).then(history.push('/'));
            }
        }else {
            alert("권한이 없습니다.")
        }
        const {data} = await axios.get('http://127.0.0.1:8000/product/');
        setProductList(data);

    };


    return (
        <div >
            <div className="list-box-1 con">
                <ul className="row">
                    {productList.map((product) => <li key={product.id} className="cell">
                                                        <div className="img-box ">
                                                            <img src={`http://localhost:8000/${product.image}/`} />
                                                        </div>
                                                        <div className="text-xl text-left">{product.name}</div>
                                                        <div className="text-red-600 text-sm text-right">{product.price}원</div>
                                                        <button className="JoinLoign-button" onClick={(e)=>{Deleteproduct(product.id, e)}}>삭제하기</button>
                                                    </li>)}
                </ul>
            </div>

        </div>
    );
}

export default Product;