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
        <div>
            <table className="table table-striped con">
                <thead>
                <tr>
                    <th className="w-1/2" scope="col">상품정보</th>
                    <th className="w-2/12">옵션</th>
                    <th className="w-1/5" scope="col">가격</th>
                    <th className="" scope="col">비고</th>
                </tr>
                </thead>
                <tbody>
                {
                    !localStorage.getItem('token')
                        ?(
                            <tr>
                            <td>로그인 먼저 하세요</td>
                            <td></td>
                            <td></td>
                            <td></td>
                            </tr>
                        )
                        :(


                            productList.map((product) => <tr>
                                    <th key={product.id} scope="row">
                                        <div className="table-img float-left">
                                            <a>
                                                <img src={`http://localhost:8000/${product.image}/`}/>
                                            </a>
                                        </div>
                                        <div>
                                            {product.name}
                                        </div>

                                    </th>

                                    <td>옵션</td>
                                    <td>{product.price}원</td>
                                    <td>
                                        <button className="JoinLoign-button" onClick={(e)=>{Deleteproduct(product.id, e)}}>삭제하기</button>
                                        <button className="JoinLoign-button">수정하기</button>
                                    </td>

                                </tr>
                            )
                        )
                }
                </tbody>
                {/*<ul className="row">*/}

                {/*    {*/}
                {/*        !localStorage.getItem('token')*/}
                {/*        ?(<p>로그인 먼저 하세요</p>)*/}
                {/*            :(*/}
                {/*                productList.map((product) => <li key={product.id} className="cell">*/}
                {/*                <div className="img-box ">*/}
                {/*                    <img src={`http://localhost:8000/${product.image}/`} />*/}
                {/*                </div>*/}
                {/*                <div className="text-xl text-left">{product.name}</div>*/}
                {/*                <div className="text-red-600 text-sm text-right">{product.price}원</div>*/}
                {/*                <button className="JoinLoign-button" onClick={(e)=>{Deleteproduct(product.id, e)}}>삭제하기</button>*/}
                {/*                </li>*/}
                {/*                )*/}
                {/*            )*/}
                {/*    }*/}
                {/*</ul>*/}
            </table>

        </div>
    );
}

export default Product;