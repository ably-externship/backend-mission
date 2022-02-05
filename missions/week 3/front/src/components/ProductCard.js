import styled from "styled-components";
import './ProductCard.css';

function ProductCard (props){

    return(
        <div className="col-4">
            <img src={props.product.main_image_url} />
            <h6>{props.product.product_name}</h6>
            <p>{props.product.price}</p>
        </div>
    )
}

export default ProductCard