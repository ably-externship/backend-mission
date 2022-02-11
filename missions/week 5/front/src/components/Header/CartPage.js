import React,{useState, useEffect} from "react";
import {Link, useHistory} from 'react-router-dom';
import axios from 'axios';

function CartPage(props) {

    const history = useHistory();
    const [productList, setProductList] = useState([]);



    useEffect(() => {
        const take = async () => {
            const {data} = await axios.get('http://127.0.0.1:8000/cart/',
                {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`,
                    },
                }
            );
            setProductList(data);
        };
        take();
    }, []);
    console.log(productList)

    const DeleteCart = async (cart_id)=> {


        await axios.delete('http://localhost:8000/cart/delete/' + cart_id + '/', {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            }
        });

        const {data} = await axios.get('http://127.0.0.1:8000/cart/', {headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            }
        });
        setProductList(data);

    };



    return (
        <div>
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
                    productList.length!==0
                        ?(
                        productList.map((cart) => <tr key={cart.id} className="border-b odd:bg-white even:bg-gray-50 odd:dark:bg-gray-800 even:dark:bg-gray-700 dark:border-gray-600">
                            <th scope="row">
                                <div className="table-img float-left">
                                    <a>
                                        <img key={cart.id} src={`http://localhost:8000/${cart.product.image}/`}/>
                                        {/*{*/}
                                        {/*    cart.product.map((pro) => <img key={pro.id} src={`http://localhost:8000/${pro.image}/`}/>)*/}
                                        {/*}*/}
                                    </a>
                                </div>
                                <div>
                                    <div key={cart.id}>{cart.product.name} </div>
                                    {/*{*/}
                                    {/*    cart.product.map((pro) => <div key={pro.id}>{pro.name} </div>)*/}
                                    {/*}*/}
                                </div>

                            </th>

                            <th>
                                <div key={cart.id}>{cart.product_option.opt1_type} :{cart.product_option.opt1_name}, 추가가격 :{cart.product_option.opt1_price}원</div>
                                {/*{*/}
                                {/*    cart.product_option.map((opt) => <div key={opt.id}>{opt.opt1_type} :{opt.opt1_name}, 추가가격 :{opt.opt1_price}원</div>*/}
                                {/*    )*/}
                                {/*}*/}
                            </th>
                            <td>
                                <div key={cart.id}>
                                    <div>정가 :{cart.product.price}원</div>
                                    <div>할인가 :{cart.product.sale_price}원</div>
                                </div>
                                {/*{*/}
                                {/*    cart.product.map((pro) =>*/}
                                {/*        <div key={pro.id}>*/}
                                {/*            <div>정가 :{pro.price}원</div>*/}
                                {/*            <div>할인가 :{pro.sale_price}원</div>*/}
                                {/*        </div>*/}
                                {/*    )*/}
                                {/*}*/}
                            </td>
                            <td>
                                <button className="JoinLoign-button" onClick={(e)=>{DeleteCart(cart.id, e)}}>삭제하기</button>
                                {/*<button className="JoinLoign-button">수정하기</button>*/}
                            </td>

                        </tr>
                        )):
                        (
                            <tr>
                            <th>1</th>
                            <td>장바구니가 비어있습니다.</td>
                            <td></td>
                            </tr>
                        )
                }
                </tbody>
            </table>
        </div>
    );
}

export default CartPage;