import './App.css';
import React, { Component } from 'react';
import Modal from './components/Modal';
import axios from "axios";

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            modal: false,
            products: [],
            activeItem: {
                name: "",
                price: 0,
                product_img: "",
            },
        };
    }

    async componentDidMount() {
        this.refreshList();
    }

    refreshList = () => {
        axios
            .get("/apis/product/")
            .then((res) => this.setState({products: res.data}))
            .catch((err) => console.log(err));
    };

    toggle = () => {
        this.setState({ modal: !this.state.modal });
    };

    handleSubmit = (item) => {
        this.toggle();

        if (item.id) {
            axios
                .put("/apis/product/${item.id}/", item)
                .then((res) => this.refreshList());
            return;
        }
            axios
                .post("/apis/product/", item)
                .then((res) => this.refreshList());
    };

    handleDelete = (item) => {
    alert("delete" + JSON.stringify(item));
        axios
            .delete("/apis/product/${item.id}/", item)
            .then((res) => this.refreshList());
    };
//    };
    createItem = () => {
        const item = { name: "", price: 0, product_img: "" };

        this.setState({ activeItem: item, modal: !this.state.modal });
    };

    editItem = (item) => {
        this.setState({ activeItem: item, modal: !this.state.modal });
    };

    render() {
        const imagestyle = {
            width: '300px',
            height: '350px',
        };
        return (
        <main className='container'>
            <div className='m-5'>
                 <div className='m-5'>
                    <button className='btn btn-primary' onClick={this.createItem}>
                        Add Product
                    </button>
                 </div>
                {this.state.products.map(item => {
                return (
                    <div key={item.id}>
                        <div className='m-5'>
                            <img src={item.product_img} style={imagestyle} />
                            <h4>{item.id}</h4>
                            <h1>{item.name}</h1>
                            <p>{item.price}</p>
                            <br />
                            <button className='btn btn-danger' onClick={() => this.handleDelete(item)}>
                                Delete
                            </button>
                        </div>
                    </div>
                )})}
                {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}

            </div>
        </main>
        );
    }
}


export default App;

