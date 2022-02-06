import { useState, useEffect } from 'react';
import axios from 'axios';
import axiosInstance from '../utils/AxiosInstance';
import { useNavigate } from 'react-router-dom';


const ProductSummary = (props) => {
    const navigate = useNavigate()
    const onClickDelete = (productId) => {

        if (window.confirm("삭제할까요??")){
            const url = 'http://127.0.0.1:8000/api/product/' + productId
            axiosInstance.delete(url)
            alert("삭제되었습니다.");
        }
    }



    return (
        <tr className='App'>
            <td>{props.id}</td>
            <td className="w-1/4"><img className="w-3/4" src={props.image_url} href ="/"/></td>
            <td>{props.name}</td>
            <td>{props.description}</td>
            <td>{props.reg_date}</td>
            <td> <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" onClick={() => onClickDelete(props.id)} type="button">
                삭제
            </button>
            </td>
        </tr>
    )
}

export default ProductSummary;