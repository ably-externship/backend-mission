function ProductOptionModal(props){
    if ( !props.show ) {
        return null
    } else {
        const options = props.productOptions
        const style = { backgroundColor : '#fff6f6' }

        return (
            <>
            <thead>
                <tr>
                <th></th>
                <th>색상</th>
                <th>사이즈</th>
                <th>추가 가격</th>
                <th>재고</th>
                <th>품절 여부</th>
                </tr>
            </thead>
                {
                options.map((option, index)=>{
                    return (
                        <tbody key={ index }>
                            <tr style={ style }>
                            <td></td>
                            <td>{ option.color_name }</td>
                            <td>{ option.size_name }</td>
                            <td>{ !option.extra_price ? 0 : Number(option.extra_price) }</td>
                            <td>{ !option.stock ? 0 : option.stock }</td>
                            <td>{ !option.is_sold_out ? '' : '품절' }</td>
                            <td colSpan={4}></td>
                            </tr>
                        </tbody>
                    )
                })
    }
            </>
        )
    }
}

export default ProductOptionModal