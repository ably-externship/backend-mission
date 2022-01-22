import { Navbar, Container, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';

function HomeNav (){

    const authState = useSelector((state) => state);
    const dispatch = useDispatch();
    
    const logout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('account_type');
        dispatch({ type : 'logout' });
    };

    return (
        <Navbar bg="light" variant="light">
            <Container>
                    {
                        authState.account_type === 'master'
                        ? <Navbar.Brand href="/">Mbly-admin</Navbar.Brand>
                        : <Navbar.Brand href="/">Mbly</Navbar.Brand>
                    }
                    {
                        authState.isLogin === false
                        ? (
                            <Nav className="me-auto">
                                <Nav.Link as={Link} to="/products/list">Products</Nav.Link>
                                <Nav.Link as={Link} to="/accounts/signup">Sign up</Nav.Link>
                                <Nav.Link as={Link} to="/accounts/login">Log In</Nav.Link>
                            </Nav>
                        )
                        : ( authState.account_type === 'user' 
                            ? (
                                <Nav className="me-auto">
                                    <Nav.Link as={Link} to="/products/list">Products</Nav.Link>
                                    <Nav.Link as={Link} to="/accounts/signup">Cart</Nav.Link>
                                    <Nav.Link onClick={logout}>Log Out</Nav.Link>
                                </Nav>
                            )
                            : (
                                <Nav className="me-auto">
                                    <Nav.Link as={Link} to="/products/list">상품 관리</Nav.Link>
                                    <Nav.Link as={Link} to="/products/list">상품 등록</Nav.Link>
                                    <Nav.Link onClick={logout}>Log Out</Nav.Link>
                                </Nav>
                            )
                        )
                    }
            </Container>
        </Navbar>
    )
}

export default HomeNav