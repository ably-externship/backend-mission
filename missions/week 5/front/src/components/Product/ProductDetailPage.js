import React, {useEffect, useState} from 'react';
import { Route, Link } from 'react-router-dom';
import axios from "axios";
import moment from "moment";

function ProductDetailPage(props) {

    // console.log(props.location.state.user_id)

    const [product, setProduct] = useState([]);
    const [qnaList, setQnaList] = useState([]);
    const [qnatitle, setQnaTitle] = useState("");
    const [qnacontent, setQnaContent] = useState("");
    const [dateChange, setDateChange] = useState("")
    const [optionId, setOptionId] = useState(1)

    useEffect(() => {
        const take = async () => {
            const {data} = await axios.get('http://localhost:8000/product/' + props.location.state.id + '/');
            setProduct(data);
        };
        take();
        const take1 = async () => {
            const {data} = await axios.get('http://localhost:8000/product/qna/' + props.location.state.id + '/');
            setQnaList(data);
        };
        take1();
    }, []);

    // console.log(qnaList)

    const handleOption = (e)=>{
        setOptionId(e.target.value);
        // console.log(optionId);
    }

    const AddCart = async()=> {
        const formData = new FormData();

        const user=props.location.state.user_id;
        const product=props.location.state.id;
        const product_option=optionId

        // if (!user){
        //     alert('로그인 먼저 해주세요')
        // }


        const data = {user: user, product: product, product_option:product_option};

        // console.log(data)

        await axios.post('http://localhost:8000/cart/create/', data,
        {headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            }
        }).then(
            alert('장바구니 추가 완료')
        )
    };

    const AddQna = async()=> {

        const user=props.location.state.user_id;
        const product=props.location.state.id;
        const title=qnatitle
        const content=qnacontent

        // if (!user){
        //     alert('로그인 먼저 해주세요')
        // }


        const data = {user: user, product: product, title:title, content:content};

        // console.log(data)

        await axios.post('http://localhost:8000/product/qna/create/', data,
            {headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                }
            }).then(
            alert('QnA 추가 완료')
        )
        const take1 = async () => {
            const {data} = await axios.get('http://localhost:8000/product/qna/' + props.location.state.id + '/');
            setQnaList(data);
        };
        take1();
    };

    return (
        <div>
            <div className="detail-box-1 con">
                <ul className="row ">

                    <li className="cell">
                        <div className="img-box">
                            <img src={`http://localhost:8000/${product.image}/`} />
                        </div>
                    </li>
                    <li className="cell">
                        <div className="detail-inf-1">
                            <h3 className="text-4xl text-left m-2" autoFocus>{product.name}</h3>

                            <h2 className="text-right line-through text-xl m-2 text-gray-500">
                                {product.price}원
                            </h2>

                            <h2 className="text-right text-red-600 text-xl m-2 ">
                                {product.sale_price}원
                            </h2>

                            <p className="text-gray-500 m-8">
                                {product.description}
                            </p>

                            옵션 :
                            <select onClick={handleOption}>
                                    {
                                        product.product_options && product.product_options.map((option) =>
                                            <option
                                                key={option.id}
                                                value={option.id}
                                            >
                                                사이즈 :{option.opt1_name} 추가금액 :{option.opt1_price} 재고 :{option.opt1_stock}
                                            </option>
                                        )
                                    }
                            </select>
                        </div>
                        <div className="buy-Button">
                            <div>
                                <input type="submit" value="구매하기" className="signUpButton m-1"/>
                            </div>
                            <button
                                onClick={AddCart}
                                className="signUpButton m-1 object-right-bottom"
                            >
                                장바구니
                            </button>
                        </div>

                    </li>
                </ul>
            </div>


            <div className="top-bn-box-1 img-box con">
                <img src="https://thumbnail8.coupangcdn.com/thumbnails/remote/q89/image/retail/images/2019/04/19/17/4/0a65530f-8c6c-4a85-8313-fd121832ea22.jpg"/>
            </div>
            <div className="qna-boxlist-1 con">
                <div className="">
                    <h3 className="font-bold text-left qna-text text-xl">Q&A</h3>
                </div>

                <table className="qna-table">
                    <thead className="bg-gray-200">
                        <tr>
                            <th className="qna-col-1 qna-th">등록일</th>
                            <th className="qna-col-2 qna-th">제목</th>
                            <th className="qna-col-3 qna-th">내용</th>
                        </tr>
                    </thead>
                    <tbody>
                    {
                        qnaList
                            ?(
                                qnaList.map((qna) => (
                                    <tr key={qna.id} className="">
                                        <td className="qna-td">{moment(qna.reg_date).format('YYYY년 MM월 DD일')}</td>
                                        <td className="qna-td">{qna.title}</td>
                                        <td className="qna-td">{qna.content}</td>
                                    </tr>
                                ))
                            ):(
                                <tr>
                                    <td className="qna-col-1 qna-th">1</td>
                                    <td className="qna-col-2 qna-th">질문이 없습니다</td>
                                    <td className="qna-col-3 qna-th"></td>
                                </tr>
                            )
                    }
                    </tbody>
                </table>

                <br/>
                <div className="qna-boxlist-2 con">
                    <div><h3 className="font-bold text-xl">질문하기</h3></div>
                    <p className="text-l">
                        구매하시려는 상품에 대해 궁금하신 점이 있으신 경우 문의해주세요.
                    </p>
                    <div className="qna-input-1">
                        <div><input className="qna-title rounded-md m-1" onChange={e => setQnaTitle(e.target.value)}
                                    placeholder="제목"/></div>
                        <div><textarea className="qna-content rounded-md m-1" onChange={e => setQnaContent(e.target.value)}
                                       placeholder="내용"></textarea></div>
                        <button onClick={AddQna} className="qna-button m-1">
                            추가하기
                        </button>
                    </div>
                </div>
                <br/>
                <br/>


            </div>


        </div>
    );
}

export default ProductDetailPage;