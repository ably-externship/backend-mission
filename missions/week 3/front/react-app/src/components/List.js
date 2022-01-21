import React, {useEffect, useState} from "react";
import Axios from "axios";
const apiUrl = "http://localhost:8000/api/products/";

function List(){
const [List, setList] = useState([]);
useEffect(() => {
       Axios.get(apiUrl)
        .then(response => {
            const { data } = response;
            console.log('loaded response :', response);
            setList(data);
        })
        .catch(error =>{

        })
    console.log("mounted");
}, []);
    return(
        <div>
            <h2>LIST</h2>
            {List.map(post =>
                <div>{JSON.stringify(List)}</div>
            )}
        </div>
    );
}

export default List;