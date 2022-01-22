import React, { useState, useEffect } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';

import { callApi } from '../axios-api';

export default function BasicTable() {
    const [productList, setProductList] = useState([]);
  
    useEffect(() => {    
        callApi('get', 'http://127.0.0.1:8000/products/').then(response => {
            const data = response.data;
            setProductList(data.data)
        }).catch(error => {
            console.log(error)
        })
    }, [])

    const productDelete = (e,id) => {
        console.log(id)
    }
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>상품 아이디</TableCell>
            <TableCell align="center">마켓명</TableCell>
            <TableCell align="center">상품 카테고리</TableCell>
            <TableCell align="center">상품명</TableCell>
            <TableCell align="center">가격</TableCell>
            <TableCell align="center">품절여부</TableCell>
            <TableCell align="center">상품 등록일</TableCell>
            <TableCell align="center">삭제</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {productList.map((row) => (
            <TableRow
              key={row.id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.id}
              </TableCell>
              <TableCell component="th" scope="row">
                {row.market_fk}
              </TableCell>
              <TableCell component="th" scope="row">
                {row.product_category}
              </TableCell>
              <TableCell align="center">{row.name}</TableCell>
              <TableCell align="center">{row.price}</TableCell>
              <TableCell align="center">{row.sold_out_yn === false ? '판매중' : '품절'}</TableCell>
              <TableCell align="center">{row.create_date}</TableCell>
              <TableCell align="center"><Button onClick={ e => {productDelete(e, row.id)}}>삭제</Button></TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}