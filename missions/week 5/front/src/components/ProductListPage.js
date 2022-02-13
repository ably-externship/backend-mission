import { useEffect, useState } from "react";
import axios from "axios";
import './ProductListPage.css';
import PaginationBtns from "./PaginationBtns.js";

function ProductList (){

    const [products, setProducts] = useState([]);
    const [pages, setPages] = useState();
    const [currentPage, setCurrentPage] = useState(1);
    const limit = 8;

    const [search, setSearch] = useState('');
    const onChangeSearch = (e) => {
        setSearch(e.target.value);
    }
    const onSubmitSearch = (e) => {
        e.preventDefault();
        setCurrentPage(1);

        axios.get("http://localhost:8000/products/list", { params : { page : currentPage, search_word : search } })
        .then((response)=>{
            const productList = response.data.product_lists;
            setProducts(productList);
            const productCounts = response.data.product_counts;
            setPages(Math.ceil(productCounts/limit));
        })
    }

    useEffect(()=>{
        axios.get("http://localhost:8000/products/list", { params : { page : currentPage, search_word : search } })
        .then((response)=>{
            const productList = response.data.product_lists;
            setProducts(productList);
            const productCounts = response.data.product_counts;
            setPages(Math.ceil(productCounts/limit));
        })
    }, [currentPage]);

    return(
        <>
        
        <div className="container">
            <div className="row">
            <div className="inputContainer">
                <form onSubmit={onSubmitSearch}>
                    <input placeholder="Search..." onChange={onChangeSearch}/>
                </form>
            </div>
                {
                    products.map((a, i)=>{
                        return (
                            <div key = {i} className="col-3">
                                <img src={a.main_image_url} />
                                <h6>{a.product_name}</h6>
                                <p>{Number(a.price)}원</p>
                            </div>
                        )
                    })
                }
            </div>
            <PaginationBtns pages={pages} currentPage={currentPage} setCurrentPage={setCurrentPage}/>
        </div>
        </>
    )
}

export default ProductList