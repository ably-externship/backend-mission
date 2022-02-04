import axios from 'axios';
import { useState, useEffect, useRef, forwardRef } from 'react';
import { Form, Button, Row, Col } from 'react-bootstrap';
import styled from 'styled-components';
import './ProductRegistration.css';

function ProductRegistration(){

    const [categories, setCategories] = useState([]);
    const [colors, setColors] = useState([]);
    const [sizes, setSizes] = useState([]);

    useEffect(()=>{
        axios.get('http://localhost:8000/categories')
        .then((response)=>{
            if ( response != null && response.data != null ) {
                setCategories(response.data.result)
            }
        })
        .catch((error)=>{
            console.log(error);
        })
        axios.get('http://localhost:8000/colors')
        .then((response)=>{
            if ( response != null && response.data != null ) {
                setColors(response.data.result)
            }
        })
        .catch((error)=>{
            console.log(error);
        })
        axios.get('http://localhost:8000/sizes')
        .then((response)=>{
            if ( response != null && response.data != null ) {
                setSizes(response.data.result)
            }
        })
        .catch((error)=>{
            console.log(error);
        })
    },[])
    
    const subcategorySelect = useRef();
    const [subcategories, setSubcategories] = useState([]);
    const [subcategoryId, setSubcategoryId] = useState(0);

    const onChangeCategory = (e) => {
        const category = categories[e.target.value];
        setSubcategories(category.subcategories);
        subcategorySelect.current.value = '0';
        setSubcategoryId(0);
    }
    const onChangeSubcategory = (e) => {
        setSubcategoryId(e.target.value);
    }

    const [productInfo, setProductInfo] = useState({ name : '', price : '', discount_price : '' });
    
    const onChangeProductInfo = (e) => {
        const { name, value} = e.target;
        setProductInfo({ ...productInfo, [name] : value });
    }

    const [mainImg, setMainImg] = useState();
    const onChangeMainImg = (e) => {
        setMainImg(e.target.files[0]);
    }

    const [detailImgs, setDetailImgs] = useState();
    const onChangeDetailImgs = (e) => {
        setDetailImgs(e.target.files);
    }

    const [option, setOption] = useState({ color : '', color_name : '', size : '', size_name : '', extra_price : '' })
    const [options, setOptions] = useState([]);

    const onChangeColor = (e) => {
        const target = e.target.value;
        if (target === 'color') {
            const copy = { ...option };
            copy.color = '';
            copy.color_name = '';
            setOption(copy);
        } else {
            const copy = { ...option };
            copy.color = colors[target].id;
            copy.color_name = colors[target].name;
            setOption(copy);
        }
    }
    const onChangeSize = (e) => {
        const target = e.target.value;
        if (target === 'size') {
            const copy = { ...option };
            copy.size = '';
            copy.size_name = '';
            setOption(copy);
        } else {
            const copy = { ...option };
            copy.size = sizes[target].id;
            copy.size_name = sizes[target].name;
            setOption(copy);
        }
    }
    const onChangeExtraPrice = (e) => {
        const copy = { ...option };
        copy.extra_price = e.target.value;
        setOption(copy);
    }
    
    const onClickOptionAdd = () => {
        const a = options.find((e)=>e.color==option.color && e.size == option.size)
        if ( !option.color || !option.size ){
            alert('색상, 사이즈를 선택해주세요.');
        } else if ( !a ){
            setOptions( [ ...options, option ] )
        } else {
            alert('이미 존재하는 상품 옵션입니다.')
        }
    }
    const onClickOptionDelete = (i) => {
        const copy = [ ...options ];
        copy.splice(i, 1);
        setOptions(copy);
    }

    const onClickRegistration = () => {
        const formData = new FormData();
        if ( !subcategoryId ) {
            alert('카테고리를 선택해주세요.')
        } else if ( !productInfo.name || !productInfo.price ) {
            alert('상품명과 가격을 입력해주세요.')
        } else if ( !mainImg ) {
            alert('메인사진을 선택해주세요.')
        } else if ( !detailImgs ) {
            alert('상세사진을 선택해주세요.')
        } else if ( options.length === 0 ) {
            alert('상품 옵션을 선택해주세요.')
        } else if ( productInfo.price && productInfo.discount_price && productInfo.price <= productInfo.discount_price ) {
            alert('할인가격은 가격보다 클 수 없습니다.')
        } else if ( productInfo.price <= 0 || productInfo.discount_price <= 0 ) {
            alert('가격은 0보다 큰 값을 입력해주세요.')
        } else {
            const data = {
                product_subcategory : subcategoryId,
                producthistory_set : [productInfo],
                productoption_set : options
            }
            formData.append('data', JSON.stringify(data))
            formData.append('main_image', mainImg)
            Array.from(detailImgs).forEach(img=>formData.append('detail_images', img))
            
            axios.post('http://localhost:8000/admin/products', formData)
            .catch((error)=>{
                console.log(error);
            })
        }
    }

    return (
        <Form className='registrationForm'>
            <Row>
                <Col>
                    <Form.Select onChange={onChangeCategory}>
                        <option value='category'>1차카테고리</option>
                        {
                            categories.map((a, i)=>{
                                return <option key={i} value={i}>{a.name}</option>
                            })
                        }
                    </Form.Select>
                </Col>
                <Col>
                    <Subcategory subcategories={subcategories} onChangeSubcategory={onChangeSubcategory} ref={subcategorySelect}/>
                </Col>
            </Row>

            <Form.Group>
                <Form.Label>상품명</Form.Label>
                <Form.Control type='text' name='name' onChange={onChangeProductInfo}/>
            </Form.Group>
            
            <Form.Group>
                <Form.Label>가격</Form.Label>
                <Form.Control type='text' name='price' onChange={onChangeProductInfo}/>
            </Form.Group>
            
            <Form.Group>
                <Form.Label>할인가격</Form.Label>
                <Form.Control type='text' name='discount_price' onChange={onChangeProductInfo}/>
            </Form.Group>

            <Form.Group>
                <Form.Label>상품 메인 사진</Form.Label>
                <Form.Control type="file" onChange={onChangeMainImg}/>
            </Form.Group>

            <Form.Group>
                <Form.Label>상품 상세 사진</Form.Label>
                <Form.Control type="file" multiple onChange={onChangeDetailImgs}/>
            </Form.Group>

            <Row className='productOption'>
                <Col>
                    <Form.Select onChange={onChangeColor}>
                        <option value='color'>색상</option>
                        {
                            colors.map((a, i)=>{
                                return <option key={i} value={i}>{a.name}</option>
                            })
                        }
                    </Form.Select>
                </Col>
                <Col>
                    <Form.Select onChange={onChangeSize}>
                        <option value='size'>사이즈</option>
                        {
                            sizes.map((a, i)=>{
                                return <option key={i} value={i}>{a.name}</option>
                            })
                        }
                    </Form.Select>
                </Col>
                <Col>
                    <Form.Group>
                        <Form.Control type='text' placeholder='옵션 추가 가격' onChange={onChangeExtraPrice}/>
                    </Form.Group>
                </Col>
                <Col xs={2}>
                    <Button variant="success" size="sm" onClick={onClickOptionAdd}>옵션 추가</Button>
                </Col>
            </Row>
            {
                options.map((a,i)=>{
                    return (
                    <OptionItem key={i}>옵션 {i+1} : {a.color_name} / {a.size_name} 추가 가격 : { !a.extra_price ? 0 : a.extra_price }
                        <Button onClick={()=>{
                            onClickOptionDelete(i)
                        }} style={{ marginLeft : 'auto' }} variant="danger" size='sm'>X</Button>
                    </OptionItem>
                )
            })
            }
            <Button variant="primary" onClick={onClickRegistration}>상품 등록</Button>
            

        </Form>
    )
}

const Subcategory = forwardRef((props, ref)=>{

    return(
        <Form.Select ref={ref} onChange={props.onChangeSubcategory}>
            <option value='0'>2차카테고리</option>
            {
                props.subcategories.map((a)=>{
                    return <option key={a.id} value={a.id}>{a.name}</option>
                })
            }
        </Form.Select>
    )

})

const OptionItem = styled.p`
    display : flex`

export default ProductRegistration