import { useState, useEffect } from "react";
import axios from "axios";
import { Table, Button } from 'react-bootstrap';
import styled from "styled-components";


function AdminProductList (){

    const [products, setProducts] = useState([]);

    useEffect(()=>{
        axios.get("http://localhost:8000/admin/products", {
            headers : {
                Authorization : localStorage.getItem('access_token')
            }
        })
        .then((response)=>{
            if ( response !== null && response.data !== null ) {
                const productList = response.data;
                setProducts(productList);
            }
        })
        .catch((error)=>{
            console.log(error);
        })
    }, []);

    const clickHandler = (param) => {
        axios.delete("http://localhost:8000/admin/products/" + String(param), {
            headers : {
                Authorization : localStorage.getItem('access_token')
            }
        })
        .then(()=>{
            window.location.reload();
        })
        .catch((error)=>{
            console.log(error);
        })
    }

    return (
        <Table striped bordered hover>
            <thead>
                <tr>
                <th>상품 id</th>
                <th>메인사진</th>
                <th>셀러</th>
                <th>상품명</th>
                <th>가격</th>
                <th>할인가</th>
                <th>품절여부</th>
                <th>진열여부</th>
                <th>삭제</th>
                </tr>
            </thead>
            {
                products.map((a, i)=>{
                    return (
                        <tbody key={i}>
                            <TableRow>
                            <td>{ a.product }</td>
                            <td><ProductImage src={ a.main_image_url }/></td>
                            <td>{ a.seller_name }</td>
                            <td>{ a.product_name }</td>
                            <td>{ Number(a.price) }</td>
                            <td>{ Number(a.discount_price) }</td>
                            { a.is_sold_out === true ? <td>품절</td> : <td></td> }
                            { a.is_displayed === true ? <td>진열중</td> : <td>미진열</td> }
                            <td><Button variant="outline-danger" onClick={()=>{clickHandler(a.product);}}>삭제</Button></td>
                            </TableRow>
                        </tbody>
                    )
                })
            }
        </Table>
    )


}

export default AdminProductList

const ProductImage = styled.img`
    width : 60px;
    height : 60px;
`
const TableRow = styled.tr`
    vertical-align : middle;`