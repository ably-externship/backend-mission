import { Navbar, Container, Nav } from 'react-bootstrap';
import { Link, Switch, Route } from 'react-router-dom';
import './App.css';
import SignupPage from './components/SignupPage.js';
import ProductList from './components/ProductListPage.js';
import KakaoLogin from './components/KakaoLogin';

function App() {

  return (
    <div className="App">
      
      <Navbar bg="light" variant="light">
        <Container>
        <Navbar.Brand href="/">Mbly</Navbar.Brand>
        <Nav className="me-auto">
          <Nav.Link as={Link} to="/products/list">Products</Nav.Link>
          <Nav.Link as={Link} to="/accounts/signup">Sign Up</Nav.Link>
          <Nav.Link href="#pricing">Log In</Nav.Link>
        </Nav>
        </Container>
      </Navbar>

      <Switch>

        <Route exact path="/">
          <div className="Jumbotron">
            <h1>2022 NEW ARRIVALS!</h1>
          </div>
        </Route>

        <Route exact path="/products/list">
          <ProductList/>
        </Route>

        <Route exact path="/accounts/signup">
          <SignupPage/>
        </Route>

      </Switch>

      

    </div>
  );
}

export default App;
