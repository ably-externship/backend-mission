import React, { useEffect, useState } from "react";
import Axios from "axios";

const apiURL = "http://127.0.0.1:8000/products/";
const accessToken = localStorage.getItem("accessToken");
const headers = { Authorization: `Bearer ${accessToken}` };

function ProductList() {
  const [productList, setProductList] = useState([]);
  useEffect(() => {
    Axios.get(apiURL, { headers: headers })
      .then((response) => {
        // console.log("res", response);
        const { data } = response;
        console.log("data", data);
        setProductList(data);
      })
      .catch((error) => {
        //erorr.response
      });
  }, []);
  const deleteClick = async (event) => {
    // console.log("delete", id);
    // console.log(id.id);
    await Axios.delete(
      `http://127.0.0.1:8000/products/${event.target.value}/`,
      {
        headers: headers,
      }
    );
    window.location.replace("/products");
  };

  return (
    <div>
      <div className="flex items-center flex-wrap ">
        {productList.map((product) => {
          const { id, market, category, name, price } = product;
          return (
            <div className="p-4 sm:w-1/4 lg:w-1/4">
              <div className="h-full border-2 border-gray-200 border-opacity-60 rounded-lg overflow-hidden">
                <img
                  className="lg:h-72 md:h-48 w-full object-cover object-center"
                  src={`https://picsum.photos/id/${id}/50/50`}
                  alt="card image"
                />
                <div className="p-6 hover:bg-indigo-600 hover:text-white transition duration-300 ease-in">
                  {id}, {market}, {category}, {name}, {price}원
                </div>
                <button
                  value={id}
                  onClick={deleteClick}
                  // onClick={() => {
                  //   deleteClick({ id });
                  // }}
                  className="p-6 hover:bg-red-600 hover:text-white transition duration-300 ease-in"
                >
                  삭제
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default ProductList;
