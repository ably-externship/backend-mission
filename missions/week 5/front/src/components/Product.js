import React,{useState,useEffect,useCallback,useMemo} from "react";
import {Link, useHistory} from 'react-router-dom';
import axios from 'axios';

function Product(props) {

    console.log(props.user_id)

    const history = useHistory();
    const [productList, setProductList] = useState([]);
    const [inputsearch, setInputSearch] = useState('');



    useEffect(() => {
        const take = async () => {
            const {data} = await axios.get('http://127.0.0.1:8000/product/',
                {
                        // headers: {
                        //     Authorization: `Bearer ${localStorage.getItem('token')}`,
                        // },
                        params:{
                            search: inputsearch,
                        }
                    }
                );
            setProductList(data);
        };
        take();
    }, [inputsearch]);
    // console.log(inputsearch)
    // console.log(productList)

    // const Deleteproduct = async (product_id)=> {
    //     if(!!localStorage.getItem('token')) {
    //         if (window.confirm('정말 삭제하시겠습니까 ?') === true) {
    //             await axios.delete('http://localhost:8000/product/delete/' + product_id + '/', {
    //                 headers: {
    //                     Authorization: `Bearer ${localStorage.getItem('token')}`,
    //                 }
    //             }).then(history.push('/'));
    //         }
    //     }else {
    //         alert("권한이 없습니다.")
    //     }
    //     const {data} = await axios.get('http://127.0.0.1:8000/product/', {headers: {
    //             Authorization: `Bearer ${localStorage.getItem('token')}`,
    //         }
    //     });
    //     setProductList(data);
    //
    // };


    return (
        <div className="">
            <div className="top-bn-box-1 img-box con">
                <img src="http://cdn.thescoop.co.kr/news/photo/202106/50977_72210_530.jpg" alt=""/>
            </div>


            <div className="flex-grow flex items-center px-3 con">
                <input
                    className="text-black" value={inputsearch}
                    onChange={e => setInputSearch(e.target.value)}
                    placeholder="찾으실 물건을 입력"
                />
            </div>

            <div className="list-box-1 con">
                <ul className="row">
                    {productList.map((product) => <li key={product.id} className="cell">
                        <Link to={{
                            pathname:`/product/${product.id}`,
                            state:{
                                id:`${product.id}`,
                                user_id : `${props.user_id}`
                            }
                        }}>
                            <div className="img-box ">
                                <img src={`http://localhost:8000/${product.image}/`} />
                            </div>
                            <div className="text-xl text-left">{product.name}</div>
                            <div className="text-sm text-right">{product.price}원</div>
                            <div className="text-red-600 text-sm text-right">{product.sale_price}원</div>
                            {/*<button className="JoinLoign-button" onClick={(e)=>{Deleteproduct(product.id, e)}}>삭제하기</button>*/}
                        </Link>

                    </li>)}
                </ul>
            </div>
        </div>
    );
}

export default Product;