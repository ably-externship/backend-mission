import React, { useState } from "react";
import axios from "axios";
// import "./RestApi.css";

function RestAPI() {
    const [text, setText] = useState([]);

    return (
        <>
            <h1> Rest API 연습 </h1>
            <div className="btn-primary m-2 p-5 position-relative">
                <form>
                <p>
                    <label>쇼핑몰 이름: &nbsp; </label>
                    <input type="text" id="name_mall" name="name_mall"></input>
                </p>
                <p>
                    <label>쇼핑몰 설명: &nbsp; </label>
                    <input type="text" id="description" name="description"></input>
                </p>
                <p>
                    <label>쇼핑몰 주소: &nbsp; </label>
                    <input type="text" id="url" name="url"></input>
                </p>
                <p>
                    <label>이미지 주소: &nbsp; </label>
                    <input type="text" id="img_url" name="img_url"></input>
                </p>
                <button
                    onClick={() => {
                        axios
                            .post("http://127.0.0.1:8000/restapi/mall-view/", {
                                "name": name_mall,
                                "description": description,
                                "url":url,
                                "img_url": img_url
                            })
                            .then(function (response) {
                                console.log(response);
                            })
                            .catch(function (error) {
                                console.log(error)
                            });
                    }}>
                    POST
                </button>
                </form>

                <button
                    onClick={() => {
                        axios
                            .get("http://127.0.0.1:8000/restapi/mall-list/")
                            .then((response) => {
                                setText([...response.data]);
                                console.log(response.data);
                            })
                            .catch(function (error) {
                                console.log(error)
                            });
                    }}>
                    Mall GET
                </button>

                <button
                    onClick={() => {
                        axios
                            .get("http://127.0.0.1:8000/restapi/itemlist/")
                            .then((response) => {
                                setText([...response.data]);
                                console.log(response.data);
                            })
                            .catch(function (error) {
                                console.log(error)
                            });
                    }}>
                    Item GET
                </button>
            </div>
            {
        text.map((e) => (
            <div className="position-relative">
                {" "}
                <div className="list m-5">
                    <span>
                        <p>{e.name}, </p>
                        <p>{e.description},</p>
                        <p>{e.url}</p>
                    </span>

                    <button
                        className="btn-delete"
                        onClick={() => {
                            axios.delete(`http://127.0.0.1:8000/mall-delete//${e.id}`);
                            setText(text.filter((text) => text.id !== e.id));
                        }}
                    >
                        DELETE
                    </button>{" "}
                </div>
            </div>
        ))
    }

        </>
    );
}

export default RestAPI;
