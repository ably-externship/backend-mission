import React, { useState } from "react";
import axios from "axios";
import "./Product.css";
import { useHistory } from "react-router-dom";
import useLocalStorage from "./accounts/useLocalStorage";


function Product() {
  const history = useHistory();
  const [text, setText] = useState([]);
  const [jwtToken, setJwtToken] = useLocalStorage("jwtToken", "");
  const apiUrl = 'http://127.0.0.1:8000/product/list';
  return (
    <>
    <div className="head">
      <h1>React with Rest API</h1>
      <div className="get_product">
        <button
          onClick={() => {
            axios
              .get("http://127.0.0.1:8000/api/products", { headers: {"Authorization" : `JWT ${jwtToken}`} })
              .then((response) => {
                setText([...response.data]);
                console.log(response.data);
                 console.log(jwtToken);

              })
              .catch(function (error) {
                console.log(error);
                if(error.response.status==401){
                    alert('로그인이 필요합니다.');

                }
              });
          }}
        >
          GET
        </button>
      </div>
      </div>
      {text.map((e) => (
        <div>
          {" "}
          <div className="list">
            <p> ID : {e.id} </p>
            <p> 이름 : {e.name} </p>
            <p> 입점사 : {e.seller} </p>
            <p> 가격 : {e.price} </p>
            <p>설명 : {e.description} </p>

            <button
              className="btn-delete"
              onClick={() => {
                axios.delete(`http://127.0.0.1:8000/api/products/${e.id}`);
                setText(text.filter((text) => text.id !== e.id));
              }}
            >
              DELETE
            </button>{" "}
          </div>
        </div>
      ))}
    </>
  );
}

export default Product;