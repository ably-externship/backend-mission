import React from 'react';
import './App.css';
import api from './api';
import ProductView from './components/ProductView';


class App extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      name: '',
      price: '',
      results: [],
    }
  }

  componentDidMount(){
    this.getProduct()
   }

   async getProduct(){
    const _results = await api.getAllProduct()
    //_results.data에는 아무 데이터가 없다. -> 비동기
    this.setState({results: _results.data})
    console.log(_results)
  }

  handlingChange = (event)=> {
    this.setState({[event.target.name]: event.target.value})
  }


  handlingSubmit = async (event) => {
    event.preventDefault() //event의 기능 -> 막는다
    let result = await api.createProduct({name: this.state.name, price: this.state.price, product_img: this.state.product_img, stock: this.state.stock})
    console.log("완료! "+ result)
    this.setState({name: '', price: 0, product_img: "", stock: 0})
    this.getProduct()
  }
  handlingDelete = async (event) => {
    await api.deleteProduct(event.target.value)
    this.getProduct()
  }

  render(){
  return (
    <div className="App">
      <div className="ProductSection">
        <h2>상품 등록하기</h2>
        <form onSubmit={this.handlingSubmit}>
        <div>
        <label for="name">상품 이름 : </label>
        <input
          type="text"
          name="name"
          value={this.state.name}
          onChange={this.handlingChange}
        />
        </div>
        <div>
        <label for="price">가격 : </label>
        <input
          type="number"
          name="price"
          value={this.state.price}
          onChange={this.handlingChange}
        />
        </div>
        <div>
        <label for="product_img">상품 이미지 url : </label>
        <input
          type="url"
          name="product_img"
          value={this.state.product_img}
          onChange={this.handlingChange}
        />
        </div>
        <div>
        <label for="stock">수량 : </label>
        <input
          type="number"
          name="stock"
          value={this.state.stock}
          onChange={this.handlingChange}
        />
        </div>
        <button type ="submit">제출하기</button>
        </form>
      </div>
      <br/>
      <hr/>

      <div className="ViewSection">
        {
          this.state.results.map((product) =>
          <div>
            <ProductView key = {product.id} id = {product.id} name = {product.name} price = {product.price} product_img = {product.product_img}
                stock = {product.stock}/>
            <button value = {product.id} onClick={this.handlingDelete}>삭제하기</button>
            <hr/>
          </div>
          )
        }
      </div>
    </div>
  );
  }
}

export default App;











//import './App.css';
//import React, { Component } from 'react';
//import Modal from './components/Modal';
//import axios from "axios";
//
//<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
//
//
//class App extends Component {
//    constructor(props) {
//        super(props);
//        this.state = {
//            modal: false,
//            products: [],
//            activeItem: {
//                name: "",
//                price: 0,
//                product_img: "",
//            },
//        };
//    }
//
//    async componentDidMount() {
//        this.refreshList();
//    }
//
//    refreshList = () => {
//        axios
//            .get("/apis/product/")
//            .then((res) => this.setState({products: res.data}))
//            .catch((err) => console.log(err));
//    };
//
//    toggle = () => {
//        this.setState({ modal: !this.state.modal });
//    };
//
//    handleSubmit = (item) => {
//        this.toggle();
//
//        if (item.id) {
//            axios
//                .put("/apis/product/${item.id}/", item)
//                .then((res) => this.refreshList());
//            return;
//        }
//            axios
//                .post("/apis/product/", item)
//                .then((res) => this.refreshList());
//    };
//
//    handleDelete = (item) => {
//    alert("delete" + JSON.stringify(item));
//        axios
//            .delete("/apis/product/${item.id}/", item)
//            .then((res) => this.refreshList());
//    };
////    };
//    createItem = () => {
//        const item = { name: "", price: 0, product_img: "" };
//
//        this.setState({ activeItem: item, modal: !this.state.modal });
//    };
//
//    editItem = (item) => {
//        this.setState({ activeItem: item, modal: !this.state.modal });
//    };
//
//    render() {
//        const imagestyle = {
//            width: '300px',
//            height: '350px',
//        };
//        return (
//        <main className='container'>
//            <div className='m-5'>
//                 <div className='m-5'>
//                    <button className='btn btn-primary' onClick={this.createItem}>
//                        Add Product
//                    </button>
//                 </div>
//                {this.state.products.map(item => {
//                return (
//                    <div key={item.id}>
//                        <div className='m-5'>
//                            <img src={item.product_img} style={imagestyle} />
//                            <h4>{item.id}</h4>
//                            <h1>{item.name}</h1>
//                            <p>{item.price}</p>
//                            <br />
//                            <button className='btn btn-danger' onClick={() => this.handleDelete(item)}>
//                                Delete
//                            </button>
//                        </div>
//                    </div>
//                )})}
//                {this.state.modal ? (
//          <Modal
//            activeItem={this.state.activeItem}
//            toggle={this.toggle}
//            onSave={this.handleSubmit}
//          />
//        ) : null}
//
//            </div>
//        </main>
//        );
//    }
//}
//
//
//export default App;
//
