import { Navbar, Container, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';

function HomeNav (){

    const loginState = useSelector((state) => state);
    const dispatch = useDispatch();
    
    const logout = () => {
        localStorage.removeItem('access_token');
        dispatch({ type : 'logout' });
        alert('로그아웃되었습니다.')
    };

    return (
        <Navbar bg="light" variant="light">
            <Container>
                <Navbar.Brand href="/">Mbly</Navbar.Brand>
                    {
                        loginState === true
                        ? (
                            <Nav className="me-auto">
                                <Nav.Link as={Link} to="/products/list">Products</Nav.Link>
                                <Nav.Link as={Link} to="/accounts/signup">Cart</Nav.Link>
                                <Nav.Link onClick={logout}>Log Out</Nav.Link>
                            </Nav>
                        )
                        : (
                            <Nav className="me-auto">
                                <Nav.Link as={Link} to="/products/list">Products</Nav.Link>
                                <Nav.Link as={Link} to="/accounts/signup">Sign up</Nav.Link>
                                <Nav.Link as={Link} to="/accounts/login">Log In</Nav.Link>
                            </Nav>
                        )
                    }
            </Container>
        </Navbar>
    )
}

export default HomeNav