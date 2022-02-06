import React, {useState, useEffect, useRef} from 'react';
import { useHistory } from 'react-router-dom';
import axios from "axios";

function Writer(props) {
    // console.log(props.loginedUserInfo.user_id);

    const history = useHistory()
    let Today = new Date();
    let date = Today.getFullYear() + "-" + Today.getMonth() + "-" + Today.getDate()

    let [goback, setGoback] = useState(false)
    let [productId, setProductID] = useState(0)
    let [market, setMarket] = useState("")
    const selectList = ["아우터", "상의", "원피스/세트", "팬츠", "스커트", "트레이닝", "가방", "신발", "패션소품", "주얼리", "언더웨어", "기타"];
    const [Selected, setSelected] = useState("");

    const [image, setImage] = useState(null);

    const [productMakeList, setProductMakeList] = useState({
        category : "",
        name : "",
        price : 0,
        sale_price : 0,
        description : "",
        image : "image",
        image_detail : "image_detail",
        is_hidden : false,
        is_sold_out : false,
        reg_date : date,
        update_date : date,
        market : props.loginedUserInfo.user_id
    });

    const [optionMakeList, setOptionMakeList] = useState({
        opt1_type : "",
        opt1_name : "",
        opt1_price : 0,
        opt1_stock : 0,
        opt2_type : "",
        opt2_name : "",
        opt2_price : 0,
        opt2_stock : 0,
        opt3_type : "",
        opt3_name : "",
        opt3_price : 0,
        opt3_stock : 0,
        reg_date : date,
        update_date : date,
    });



    const ImageonChange = (e) => {
        setImage(e.target.files[0]);
    }



    const Insertproduct = async ()=> {
        setGoback(true)
        const formData = new FormData();

        formData.append('category', Selected);
        formData.append('name', productMakeList["name"]);
        formData.append('price', productMakeList["price"]);
        formData.append('sale_price', productMakeList["sale_price"]);
        formData.append('description', productMakeList["description"]);
        formData.append('image', productMakeList["image"]);
        formData.append('image_detail', productMakeList["image_detail"]);
        formData.append('is_hidden', productMakeList["is_hidden"])
        formData.append('is_sold_out', productMakeList["is_sold_out"]);
        formData.append('reg_date', productMakeList["reg_date"]);
        formData.append('update_date', productMakeList["update_date"])
        formData.append('market', productMakeList["market"]);


        await axios.post('http://localhost:8000/product/create/', formData, {headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            }
        })


    };

    const Insertoption = async ()=> {


        // console.log(productMakeList["name"])
        const find = async () => {
            const {data} = await axios.get('http://localhost:8000/product/find/' + productMakeList["name"] + '/',
                {headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`,
                    }
                });
            setProductID(data['id']);
            // console.log(data['id'])

            const formData = new FormData();

            formData.append('opt1_type', optionMakeList["opt1_type"]);
            formData.append('opt1_name', optionMakeList["opt1_name"]);
            formData.append('opt1_price', optionMakeList["opt1_price"]);
            formData.append('opt1_stock', optionMakeList["opt1_stock"]);
            formData.append('product', data['id']);


            await axios.post('http://localhost:8000/product/option/create/', formData, {headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                }
            });
            alert('옵션 추가 완료')
        };
        find();


    };

    const Nextpage = async ()=> {
        alert('상품을 추가하였습니다.')
        history.push('/')
    }

    return (
        <>
            {
                goback === false
                ?(
                        <div className="write-product-1">
                            <div className="">
                                <span className="menu">상품 등록창</span>
                                <article className="detail-box-1">
                                    <ul className="row">
                                        <li className="cell">

                                            <div className="">
                                                <input type="text" placeholder="상품명을 입력하세요" onChange={e => setProductMakeList({...productMakeList, name: e.target.value})} className="input-1"></input>
                                            </div>
                                            <div className="">
                                                <textarea placeholder="상품에 대한 설명을 입력하세요" onChange={e => setProductMakeList({...productMakeList, description: e.target.value})} className="input-2"></textarea>
                                            </div>

                                        </li>
                                        <li className="cell">
                                            <div className="">
                                                <input type="number" placeholder="정가를 입력하세요" onChange={e => setProductMakeList({...productMakeList, price: e.target.value})} className="input-1"></input>
                                            </div>
                                            <div className="">
                                                <input type="number" placeholder="할인가를 입력하세요" onChange={e => setProductMakeList({...productMakeList, sale_price: e.target.value})} className="input-1"></input>
                                            </div>

                                            <div className="detail-box-2">
                                                <ul className="row">
                                                    <li className="cell">
                                                        <select onChange={(e)=>{setSelected(e.target.value)}} value={Selected}>{selectList.map((item) => (
                                                            <option value={item} key={item}>
                                                                {item}
                                                            </option>
                                                        ))}
                                                        </select>
                                                    </li>
                                                    <li className="cell">
                                                        <div className="m-4">
                                                            <h3>이미지 추가</h3>
                                                            <input type="file" onChange = {e => setProductMakeList({...productMakeList, image: e.target.files[0]})}/>
                                                        </div>

                                                        <div className="m-4">
                                                            <h3>상세 이미지 추가</h3>
                                                            <input type="file" onChange = {e => setProductMakeList({...productMakeList, image_detail: e.target.files[0]})}/>
                                                        </div>


                                                    </li>
                                                </ul>

                                            </div>


                                        </li>

                                    </ul>
                                </article>
                                <article className="">
                                    <footer className="flex">
                                        <button className="button-2 m-2" onClick={Insertproduct}>등록하기</button>
                                        <button className="button-2 m-2" onClick={()=>{history.goBack()}}>뒤로 가기</button>
                                    </footer>
                                </article>
                            </div>
                        </div>
                ):
                (
                    <div className="write-product-2">
                        <div className="">
                            <span className="menu m-2">옵션 등록창</span>
                            <article className="detail-box-1">
                                        <div className="">
                                            <input type="text" placeholder="유형을 입력하세요(ex. 사이즈)" onChange={e => setOptionMakeList({...optionMakeList, opt1_type: e.target.value})} className="input-1"></input>
                                        </div>
                                        <div className="">
                                            <input type="text" placeholder="유형에 대한 정보를 입력하세요" onChange={e => setOptionMakeList({...optionMakeList, opt1_name: e.target.value})} className="input-1"></input>
                                        </div>
                                        <div className="">
                                            <input type="number" placeholder="추가가격을 입력하세요" onChange={e => setOptionMakeList({...optionMakeList, opt1_price: e.target.value})} className="input-1"></input>
                                        </div>
                                        <div className="">
                                            <input type="number" placeholder="재고를 입력하세요" onChange={e => setOptionMakeList({...optionMakeList, opt1_stock: e.target.value})} className="input-1"></input>
                                        </div>
                            </article>
                            <article>
                                <footer className="flex">
                                    <button className="button-2 m-2" onClick={Insertoption}>옵션추가</button>
                                    <button className="button-2 m-2" onClick={Nextpage}>최종 등록</button>
                                    <button className="button-2 m-2" onClick={()=>{setGoback(false)}}>나가기</button>
                                </footer>
                            </article>
                        </div>
                    </div>
                )

            }


        </>
    )
}

export default Writer;