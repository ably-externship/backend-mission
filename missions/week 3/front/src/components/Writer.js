import React, {useState, useEffect, useRef} from 'react';
import { useHistory } from 'react-router-dom';
import axios from "axios";

function Writer(props) {

    const history = useHistory()
    let Today = new Date();
    let date = Today.getFullYear() + "-" + Today.getMonth() + "-" + Today.getDate()

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
        market : 1
    });


    const ImageonChange = (e) => {
        setImage(e.target.files[0]);
    }



    const Insertproduct = async ()=> {
        const formData = new FormData();

        formData.append('category', productMakeList["category"]);
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
        }).then(history.push('/'))
            .then(history.go(0));
    };

    return (
        <div>
            상품 등록창
            <div className="detail-box-1">
                <ul className="row">
                    <li className="cell">
                        <h3>이미지 추가</h3>
                        <input type="file" onChange = {e => setProductMakeList({...productMakeList, image: e.target.files[0]})}/>
                        <h3>상세 이미지 추가</h3>
                        <input type="file" onChange = {e => setProductMakeList({...productMakeList, image_detail: e.target.files[0]})}/>
                    </li>
                    <li className="cell">
                        카테고리 :
                        <select onChange={e => setProductMakeList({...productMakeList, category: e.target.value})} value={Selected}>{selectList.map((item) => (
                                <option value={item} key={item}>
                                    {item}
                                </option>
                            ))}
                        </select>
                        <div className="">
                            상품명 :<input onChange={e => setProductMakeList({...productMakeList, name: e.target.value})}></input>
                        </div>
                        <div className="">
                            상세 설명 :<textarea onChange={e => setProductMakeList({...productMakeList, description: e.target.value})}></textarea>
                        </div>
                        <div className="">
                            정가 :<input onChange={e => setProductMakeList({...productMakeList, price: e.target.value})}></input>
                        </div>
                        <div className="">
                            할인가 :<input onChange={e => setProductMakeList({...productMakeList, sale_price: e.target.value})}></input>
                        </div>
                    </li>
                </ul>
            </div>
            <article className="write-container">
                <footer className="post-comment">
                    <button className="exit-btn transparent-btn" onClick={()=>{history.goBack()}}>✔ 나가기</button>
                    <div>
                        <button className="upButton" onClick={
                            Insertproduct
                            // handleEffect(handleSubmit)
                            // setGoback(false)
                        }>등록하기</button>
                    </div>
                </footer>
            </article>
        </div>
    );
}

export default Writer;