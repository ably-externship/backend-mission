// axios 를 사용하는 js
import axios from "axios"

axios.defaults.baseURL = "http://127.0.0.1:8000/apis"


export default {
    // 모든 상품 불러오기
    getAllProduct(){
        return axios.get('/product/')
    }
    ,
    // 상품 작성하기
    createProduct(data){
        return axios.post('/product/', data)
    },
    // 상품 삭제하기
    deleteProduct(id){
        return axios.delete('/product/'+String(id))
    },

}