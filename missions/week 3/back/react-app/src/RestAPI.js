import React, { useState } from "react";
import axios from "axios";
import "./RestAPI.css";


function RestAPI() {
  const [text, setText] = useState([]);

  return (
    <>
      <h1>REST API</h1>
      <div className="btn btn-primary">
        <button
          onClick={() => {
            axios
              .get("http://127.0.0.1:8000/api/products/")
              .then((response) => {
                setText([...response.data]);
                console.log(response.data);
              })
              .catch(function (error) {
                console.log(error);
              });
          }}
        >
          GET
        </button>
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

export default RestAPI;