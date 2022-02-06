import React from "react";
import styled from 'styled-components';
import axios from 'axios';


const ProductBlock = styled.li`
    margin-bottom: 15px;
    border-bottom: 1px solid #facae1;

    overflow: hidden;
    img {
      width: 100px;
      height: auto;
      float: left;
    }
    div {
        padding-left: 20px;
        float: left;
    }
    button {
        margin-right: 20px;
        float: right;
    }
`;

const deleteProduct = (e) => {
    console.log(e.target.value);
    let t = e.target.value;
    let check = window.confirm('상품코드 : ' + e.target.value + ' 삭제하시겠습니까?');
    if(check){
        const response = axios.delete(
            'http://localhost:8000/api/product/' + t
          );
        console.log(response);
        window.alert("삭제하였습니다.");
        return window.location.href = "/";
    } else {
        window.alert("취소하였습니다.");
    }
  };


function ProductCard({ ProductID, ImageURL, ProductName, Price, Shop }) {
  return (
    <ProductBlock key={ProductID} id={ProductID}>
        <img src={ImageURL} alt="" />
        <div>
        <p>
            상품명 : <span>{ProductName}</span>
        </p>
        <p> 상품 id: {ProductID}  </p>
        <p>가격 : {Price}</p>
        <p>판매 쇼핑몰 코드 : {Shop}</p>
        </div>
        
        <button className="btn btn-outline-danger" value={ProductID} onClick={deleteProduct}>삭제</button>
        
    </ProductBlock>
  );
}

export default ProductCard;