import { useState, useEffect,useRef } from 'react';
import axios from 'axios';
import ProductSummary from './summary';
import AxiosInstance from '../utils/AxiosInstance'
import Modal from './modal'
import './modal.css'
function ProductList() {
  const [products, setProducts] = useState();
  const [loading, setLoading] = useState(true);
  const [openModal, setOpenModal] = useState(false)
  const el = useRef()
  

  // const handleCloseModal = (e) => {
  //   console.log("chedck")
  //   console.log(e)
  //   console.log("target",el.current.contains(e.target))
  //   if (el.current && !el.current.contains(e.target)) {
  //     console.log("da")
  //     setOpenModal(true);
  //   }
  // }
  
  // useEffect(() => {
  //   console.log("lciek")
  //   window.addEventListener('click', handleCloseModal);
  //   return () => {
  //     window.removeEventListener('click', handleCloseModal)
  //   };
  // }, [])


  // // BodyBlackoutStyle
  // const BodyBlackoutStyle = ({ onSetIsVisible }) => {
  //   return (
  //     <div
  //       className="body-blackout-style"
  //       onClick={() => onSetIsVisible(false)}
  //     ></div>
  //   );
  // };

  
  useEffect(() => {
    const take = async () => {
      const { data } = await AxiosInstance.get('product/market');
      setProducts(data);
      setLoading(false);
    };
    take();
  }, []);







  if (loading) return <div>Loading...</div>;


  return (
    <ul>
      {/* {product_list} */}
      <div className="container grid m-10" >

        <button className="w-20 bg-green-500 hover:bg-blue-700 text-white font-bold py-2 rounded focus:outline-none focus:shadow-outline" onClick={()=>setOpenModal(true)}>상품추가</button>
        {/* {openModal && <BodyBlackoutStyle closeModal={setOpenModal}/>} */}
        {/* {openModal && <Modal  closeModal={setOpenModal} />} */}
        <table class="table-auto">
          <thead>
            <tr>
              <th>id</th>
              <th>사진</th>
              <th>이름</th>
              <th>설명</th>
              <th>등록일</th>
              <th>삭제</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product) => (
              //  <li key={product.id}>{product.name}</li>
              <ProductSummary
                id={product.id}
                name={product.name}
                description={product.description}
                image_url={"http://localhost:8000" + product.image}
                reg_date={product.reg_date}
                product ={product}
              />
            ))}
          </tbody>
        </table>
      </div>

    </ul>

  );

}




export default ProductList;