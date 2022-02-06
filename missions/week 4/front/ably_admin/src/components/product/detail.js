function ProductList(){
    return (
      <div className="modal">
          <h4>{ name }</h4>
          <h4>{ price }</h4>
          <h4>{ description }</h4>
          <h4>{ image }</h4>
          <h4>{ reg_date }</h4>
          <h4>{ update_date }</h4>
          <h4>{ market }</h4>
          <h4>{ category }</h4>
          <h4>{ sale_price }</h4>
          <h4>{ is_deleted }</h4>
          <h4>{ deleted_date }</h4>
          <h4>{ is_hidden }</h4>
          <h4>{ hit_count }</h4>
          <h4>{ like_count }</h4>
        </div>
    )
  }
export default ProductList;