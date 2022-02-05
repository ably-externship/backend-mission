import { useEffect, useState } from "react";
import axios from "axios";
import './ProductListPage.css';
import PaginationBtns from "./PaginationBtns.js";

function ProductList (){

    const [products, setProducts] = useState([]);
    const [pages, setPages] = useState();
    const [currentPage, setCurrentPage] = useState(1);
    const limit = 9;

    useEffect(()=>{
        axios.get("http://localhost:8000/products/list", { params : { page : currentPage } })
        .then((response)=>{
            const productList = response.data.product_lists;
            setProducts(productList);
            const productCounts = response.data.product_counts;
            setPages(Math.ceil(productCounts/limit));
        })
    }, [currentPage]);

    return(
        <div className="container">
            <div className="row">
                {
                    products.map((a, i)=>{
                        return (
                            <div key = {i} className="col-4">
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
    )
}

export default ProductList