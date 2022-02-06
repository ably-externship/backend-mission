import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }
  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
        <Modal isOpen={true} toggle={toggle}>
            <ModalHeader toggle={toggle}>Listing</ModalHeader>
            <ModalBody>
                <Form>
                    <FormGroup>
                        <Label for='product-name'>Name</Label>
                        <Input
                            type="text"
                            id="product-name"
                            name="name"
                            value={this.state.activeItem.name}
                            onChange={this.handleChange}
                            placeholder="Enter Product Name"
                        />
                    </FormGroup>
                    <FormGroup>
                        <Label for='product-price'>Price</Label>
                        <Input
                            type="number"
                            id="product-titpricele"
                            name="price"
                            value={this.state.activeItem.price}
                            onChange={this.handleChange}
                            placeholder="Enter Product Price"
                        />
                    </FormGroup>
                    <FormGroup>
                        <Label for='product-name'>Product Image URL</Label>
                        <Input
                            type="url"
                            id="product-img"
                            name="product_img"
                            value={this.state.activeItem.product_img}
                            onChange={this.handleChange}
                            placeholder="Enter Product Image"
                        />
                    </FormGroup>
                </Form>
            </ModalBody>
            <ModalFooter>
                <Button
                    color="success"
                    onClick={() => onSave(this.state.activeItem)}
                >
                    Save
                </Button>
            </ModalFooter>
        </Modal>
    )
  }
}
