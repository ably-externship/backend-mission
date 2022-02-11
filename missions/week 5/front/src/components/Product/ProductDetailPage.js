import React, {useEffect, useState} from 'react';
import { Route, Link } from 'react-router-dom';
import axios from "axios";
import moment from "moment";

function ProductDetailPage(props) {

    // console.log(props.location.state.user_id)

    const [product, setProduct] = useState([]);
    const [qnaList, setQnaList] = useState([]);
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



    const handleOption = (e)=>{
        setOptionId(e.target.value);
        // console.log(optionId);
    }

    const AddCart = async()=> {
        const formData = new FormData();

        const user=props.location.state.user_id;
        const product=props.location.state.id;
        const product_option=optionId

        if (!user){
            alert('로그인 먼저 해주세요')
        }


        const data = {user: user, product: product, product_option:product_option};

        // console.log(data)

        await axios.post('http://localhost:8000/cart/create/', data,
        {headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            }
        })
        alert('장바구니 추가 완료')
        // console.log(formData)
    };


    return (
        <div>
            <div className="detail-box-1 con">
                <ul className="row ">

                    <li className="cell">
                        <div className="detail-img-1">
                            <img src={`http://localhost:8000/${product.image}/`} />
                        </div>
                    </li>
                    <li className="cell">
                        <div className="detail-inf-1">
                            <h3 className="text-4xl text-left">{product.name}</h3>

                            <h2 className="text-right line-through">
                                {product.price}원
                            </h2>

                            <h2 className="text-right">
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
                            {/*<div className="object-right-bottom">*/}
                            {/*    <input type="submit" value="장바구니" className="signUpButton m-1 object-right-bottom"/>*/}
                            {/*</div>*/}
                        </div>

                    </li>
                </ul>
            </div>


            <div className="top-bn-box-1 img-box con">
                <img
                    src="https://thumbnail8.coupangcdn.com/thumbnails/remote/q89/image/retail/images/2019/04/19/17/4/0a65530f-8c6c-4a85-8313-fd121832ea22.jpg"
                    alt=""/>
            </div>
            <div className="qna-boxlist-1 con">
                <div>
                    <h3 className="font-bold">Q&A</h3>
                </div>
                <div>
                    <table className="con">
                        <thead className="bg-gray-200">
                            <tr>
                                <th className="w-1/2" scope="col">등록일</th>
                                <th className="w-2/12">제목</th>
                                <th className="w-1/5" scope="col">내용</th>
                            </tr>
                        </thead>
                        <tbody>
                        {
                            qnaList
                                ?(
                                    qnaList.map((qna) => (
                                        <tr key={qna.id} className="">
                                            <th>{moment(qna.reg_date).format('YYYY년 MM월 DD일')}</th>
                                            <td>{qna.title}</td>
                                            <td>{qna.content}</td>
                                        </tr>
                                    ))
                                ):(
                                    <tr>
                                        <th>1</th>
                                        <td>질문이 없습니다</td>
                                        <td></td>
                                    </tr>
                                )
                        }
                        </tbody>
                    </table>
                </div>
                <br/>
                {/*<div><h3 className="font-bold">질문하기</h3></div>*/}
                {/*<p>*/}
                {/*    구매하시려는 상품에 대해 궁금하신 점이 있으신 경우 문의해주세요.*/}
                {/*</p>*/}
                {/*<form className="qna-input-1" method="POST" action="{% url 'createQna' product.id %}">*/}
                {/*    <div><input className="qna-title outline-black rounded-md m-2" name="title" type="text"*/}
                {/*                placeholder="제목" autoFocus required value=""/></div>*/}
                {/*    <div><textarea className="qna-content outline-black rounded-md m-2" name="content" type="textarea"*/}
                {/*                   placeholder="내용" required value=""></textarea></div>*/}
                {/*    <div><input className="border-black m-2" type="submit" value="등록하기"/></div>*/}
                {/*</form>*/}

            </div>


        </div>
    );
}

export default ProductDetailPage;