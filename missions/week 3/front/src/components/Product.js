import React,{useState, useEffect} from 'react';
import {Link, useHistory} from 'react-router-dom';
import axios from 'axios';

function Product(props) {

    const history = useHistory();

    const [productList, setProductList] = useState([]);

    useEffect(() => {
        const take = async () => {
            const {data} = await axios.get('http://127.0.0.1:8000/product/',{headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`,
                    }
                });
            setProductList(data);
            // console.log(data);
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
        const {data} = await axios.get('http://127.0.0.1:8000/product/', {headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            }
        });
        setProductList(data);

    };


    return (
        <div className="">
            {
                !localStorage.getItem('token')
                    ?(
                        <p>로그인 먼저 하세요</p>
                    )
                    :(
                        <table className="con">
                            <thead className="bg-gray-200">
                            <tr>
                                <th className="w-1/2" scope="col">제품정보</th>
                                <th className="w-2/12">옵션</th>
                                <th className="w-1/5" scope="col">가격</th>
                                <th className="" scope="col">비고</th>
                            </tr>
                            </thead>
                            <tbody>
                            {
                                productList.map((product) => <tr key={product.id} className="border-b odd:bg-white even:bg-gray-50 odd:dark:bg-gray-800 even:dark:bg-gray-700 dark:border-gray-600">
                                        <th key={product.id} scope="row">
                                            <div className="table-img float-left">
                                                <a>
                                                    <img src={`http://localhost:8000/${product.image}/`}/>
                                                </a>
                                            </div>
                                            <div>
                                                제품명 : {product.name}
                                            </div>

                                        </th>

                                        <th>
                                            {
                                                product.product_options.map((option) => <div key={option.id}>사이즈 :{option.opt1_name} 추가금액 :{option.opt1_price} 재고 :{option.opt1_stock} </div>)
                                            }
                                        </th>
                                        <td>{product.price}원</td>
                                        <td>
                                            <button className="JoinLoign-button" onClick={(e)=>{Deleteproduct(product.id, e)}}>삭제하기</button>
                                            <button className="JoinLoign-button">수정하기</button>
                                        </td>

                                    </tr>
                                )
                            }
                            </tbody>
                        </table>
                    )
            }
        </div>
    );
}

export default Product;