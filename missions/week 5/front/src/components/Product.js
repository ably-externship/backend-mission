import React,{useState,useEffect,useCallback,useMemo} from "react";
import {Link, useHistory} from 'react-router-dom';
import axios from 'axios';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";

function Product(props) {


    const history = useHistory();
    const [productList, setProductList] = useState([]);
    const [recommandList, SetRecommandList] =useState([]);
    const [inputsearch, setInputSearch] = useState('');
    const [category, setCategory] = useState('전체');



    useEffect(() => {
        const take = async () => {
            const {data} = await axios.get('http://127.0.0.1:8000/product/',
                {
                        // headers: {
                        //     Authorization: `Bearer ${localStorage.getItem('token')}`,
                        // },
                        params:{
                            search: inputsearch,
                            category:category
                        }
                    }
                );
            setProductList(data);
            // console.log(productList)
            if (props.isAuthenticated){
                const {data} = await axios.get('http://127.0.0.1:8000/product/recommand/',
                    {
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    }
                );
                SetRecommandList(data);
            }

        };
        take();
    }, [inputsearch]);
    // console.log(inputsearch)
    // console.log(recommandList)

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

    const ChangeProduct = async ()=> {
        // console.log(category)
        const find = async () => {
            const {data} = await axios.get('http://127.0.0.1:8000/product/',
                {
                    // headers: {
                    //     Authorization: `Bearer ${localStorage.getItem('token')}`,
                    // },
                    params:{
                        search: inputsearch,
                        category:category
                    }
                }
            );
            setProductList(data);
        }
        find()
    };


    return (
        <div className="">

            <div className="top-bn-box-1 img-box con">
                <img src="http://cdn.thescoop.co.kr/news/photo/202106/50977_72210_530.jpg" alt=""/>
            </div>
            {
                props.isAuthenticated === true
                    ?
                    (
                        <div>
                            {/*<FontAwesomeIcon icon={fa1}/>*/}
                            <p className="list-text text-xl text-left font-bold con">회원님을 위한 추천 상품</p>
                            <div className="recom-list-box-1 con">
                                <ul className="row">
                                    {recommandList.map((product) => <li key={product.id} className="cell">
                                        <Link to={{
                                            pathname:`/product/${product.id}`,
                                            state:{
                                                id:`${product.id}`,
                                                user_id : `${props.user_id}`
                                            }
                                        }}>
                                            <div className="img-box ">
                                                <img src={`http://localhost:8000/${product.image}/`}/>
                                                <div className="text">
                                                    <p>추천</p>
                                                </div>
                                            </div>
                                            <div className="list-text text-l text-left">{product.name}</div>
                                            <div className="text-sm text-right line-through">{product.price}원</div>
                                            <div className="text-red-600 text-sm text-right">{product.sale_price}원</div>
                                            {/*<button className="JoinLoign-button" onClick={(e)=>{Deleteproduct(product.id, e)}}>삭제하기</button>*/}
                                        </Link>

                                    </li>)}
                                </ul>
                            </div>

                        </div>


                    )

                    : null
            }

            <br/>

            <div>
                <div className="ca-list-box-1 con">
                    <ul className="row con">
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('전체')
                            ChangeProduct()}}><a>전체</a></li>
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('아우터')
                            ChangeProduct()}}><a>아우터</a></li>
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('상의')
                            ChangeProduct()}}><a>상의</a></li>
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('원피스/세트')
                            ChangeProduct()}}><a>원피스/세트</a></li>
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('팬츠')
                            ChangeProduct()}}><a>팬츠</a></li>
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('스커트')
                            ChangeProduct()}}><a>스커트</a></li>
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('트레이닝')
                            ChangeProduct()}}><a>트레이닝</a></li>
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('가방')
                            ChangeProduct()}}><a>가방</a></li>
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('신발')
                            ChangeProduct()}}><a>신발</a></li>
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('패션소품')
                            ChangeProduct()}}><a>패션소품</a></li>
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('주얼리')
                            ChangeProduct()}}><a>주얼리</a></li>
                        <li className="cell" onClick={(e)=>{
                            e.preventDefault();
                            setCategory('언더웨어')
                            ChangeProduct()}}><a>언더웨어</a></li>
                        {/*<li className="cell"><a>기타</a></li>*/}
                    </ul>
                </div>
            </div>

            <div className="flex-grow flex items-center px-3 con">
                <div className="bg-gray-200">
                    <input
                        className="text-black bg-gray-200" value={inputsearch}
                        onChange={e => setInputSearch(e.target.value)}
                        placeholder="찾으실 물건을 입력"
                    />
                    <FontAwesomeIcon icon={faSearch}/>
                </div>

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
                            <div className="list-text text-l text-left">{product.name}</div>
                            <div className="text-sm text-right line-through">{product.price}원</div>
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