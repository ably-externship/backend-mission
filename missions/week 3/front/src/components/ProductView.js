import  React, { Component } from 'react'

export default class ProductView extends Component{
    render(){
        const {id, name, price, product_img, stock} = this.props
        return(
            <div>
                {id}
                <img src={product_img} width='300px' height='350px' />
                <h3>{name}</h3>
                <p>{price}</p>
                <p>{stock}수량</p>
            </div>
        )
    }
}