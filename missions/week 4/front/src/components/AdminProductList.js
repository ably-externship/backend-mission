import { useState, useEffect } from "react";
import axios from "axios";
import { Table, Button } from 'react-bootstrap';
import styled from "styled-components";
import ProductOptionModal from "./ProductOptionModal.js";


function AdminProductList (){

    const [products, setProducts] = useState([]);
    const [modalVisibleId, setModalVisibleId] = useState('');
    const [productOptions, setProductOptions] = useState([]);

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

    const onClickDelete = (productId) => {
        axios.delete("http://localhost:8000/admin/products/" + String(productId), {
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
    const onClickOption = (productId, options) => {
        if ( !modalVisibleId || modalVisibleId !== productId ) {
            setProductOptions(options)
            setModalVisibleId(productId)
        } else {
            setModalVisibleId('')
        }
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
                <th>옵션</th>
                <th>삭제</th>
                </tr>
            </thead>
            {
                products.map((product, index)=>{
                    return (
                        <>
                        <tbody>
                            <TableRow>
                            <td>{ product.product_id }</td>
                            <td><ProductImage src={ product.main_image_url }/></td>
                            <td>{ product.seller_name }</td>
                            <td>{ product.product_name }</td>
                            <td>{ Number(product.price) }</td>
                            <td>{ Number(product.discount_price) }</td>
                            <td>{ !product.is_sold_out ? '' : '품절' }</td>
                            <td>{ !product.is_displayed ? '미진열' : '진열중' }</td>
                            <td><Button onClick={()=>{
                                onClickOption(product.product_id, product.product.productoption_set)
                            }
                        }>{ !modalVisibleId || modalVisibleId !== product.product_id ? '열기' : '닫기' }</Button></td>
                            <td><Button variant="outline-danger" onClick={()=>{ onClickDelete(product.product_id) }}>삭제</Button></td>
                            </TableRow>
                        </tbody>

                            <ProductOptionModal 
                            show={ modalVisibleId === product.product_id }
                            productOptions={ productOptions }/>

                        </>
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