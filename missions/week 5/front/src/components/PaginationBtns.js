import { Pagination } from 'react-bootstrap';


function PaginationBtns(props){

    const items = [];
    const style = { display : 'inline-flex' }
    
    for (let number = 1; number <= props.pages; number++){
        items.push(
            <Pagination.Item key={number} active={number===props.currentPage} onClick={()=>{
                props.setCurrentPage(number);
            }}>
                {number}
            </Pagination.Item>
        )
    }

    const onClickFirst = () => {
        props.setCurrentPage(1);
    }
    const onClickLast = () => {
        props.setCurrentPage(props.pages);
    }

    return(
            <Pagination style={ style }>
                <Pagination.First onClick={onClickFirst}/>
                <Pagination.Prev />
                {
                    items.map((a)=>{ return a })
                }
                <Pagination.Next />
                <Pagination.Last onClick={onClickLast}/>
            </Pagination>
    )
}

export default PaginationBtns