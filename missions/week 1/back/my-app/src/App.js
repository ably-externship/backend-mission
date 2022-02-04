import logo from './logo.svg';
import './App.css';
// import {useEffect, useState} from 'react';
// import { BrowserRouter as Router, Route, Routes ,Link, useLocation } from "react-router-dom";
// import { QueryClient, QueryClientProvider, useQuery } from 'react-query';

import React, { useState,useEffect } from "https://cdn.skypack.dev/react";
import ReactDOM from "https://cdn.skypack.dev/react-dom";
import {
  QueryClient,
  QueryClientProvider,
  useQuery,
    useMutation
} from "https://cdn.skypack.dev/react-query";
import {
  HashRouter as Router,
  Switch,
  Route,
  Link,
  useLocation
} from "https://cdn.skypack.dev/react-router-dom@5";
import classnames from "https://cdn.skypack.dev/classnames";
import {
  RecoilRoot,
  atom,
  useRecoilState,
  useRecoilValue
} from "https://cdn.skypack.dev/recoil";

import axios from 'axios';

function Counter({number}){
  return (
    <div>test {number}</div>
  )
}

const queryClient = new QueryClient();

function useQueryParams() {
  return new URLSearchParams(useLocation().search);
}

const deleteProduct = async item => {
    console.log(item)
    try{
        return await (
            await fetch(`http://localhost:8000/product/admin/${item.id}`,
                {method:'DELETE'}
                )
        ).json();
    }catch (err){
        throw new Error(err);
    }
}

//삭제, 수정
function PokeDetailPage ({ history }) {
  const goBack = () => {
    history.goBack();
  };

  //delete mutation
  const {mutate,
      mutateAsync,
      isLoading: isDeletingItem,
      error: deleteError} = useMutation(deleteProduct, {
          onsuccess : (data, variables, context) => {
              console.log(data);
              window.location.replace('http://localhost:3000/#/');
              window.location.href('http://localhost:3000/#/');

          }
  })


  const queryParams = useQueryParams();
  const id = parseInt(queryParams.get("id"));

  const {
    isLoading: pokemonDetailIsLoading,
    error: pokemonDetailError,
    data: pokemonDetailData
  } = useQuery(`pokemon/${id}`, () =>
    fetch(`http://localhost:8000/product/img/${id}`,
        ).then((res) => res.json())
  );


  if (pokemonDetailError || deleteError)
    return "An error has occurred: " + pokemonDetailError.message;

  if (pokemonDetailIsLoading) return "Loading...";

  return (
    <>
      <h1 className="py-2 flex font-bold bg-gray-500 text-white sticky top-0">
        <div onClick={goBack} class="flex-1 pl-2 cursor-pointer">
          뒤로가기
        </div>
        <div>{id}번 상품</div>

        <div class="flex-1"></div>
           <>
          {isDeletingItem ? <p>DeletingItem...</p> : null}
              <button onClick={() => mutate({id:id})} >삭제</button>
               </>
      </h1>
        {!pokemonDetailData ? <div>Loading...</div>:
            <>
          <div class="flex justify-center p-10">
            <img
              src= {pokemonDetailData.img_url}
            />
          </div>
              <div className="px-2 mt-2"></div>
                 <>
          {isDeletingItem ? <p>DeletingItem...</p> : null}
              <button onClick={() => mutate({id:id})} className="btn btn-block btn-secondary">삭제</button>
               </>
              <ul>
        {/*{pokemonDetailData.map((row, index) => (*/}
        {/*  <li className="px-2 mt-2" key={index}>*/}
        {/*    기술 {index + 1}&nbsp;:&nbsp;{row.img_url}*/}
        {/*  </li>*/}
        {/*))}*/}
      </ul>
                </>
}
    </>
  );
};

const pokesAtom = atom({
  key: "app/pokes",
  default: []
});

const pokesOffsetAtom = atom({
  key: "app/pokesOffset",
  default: 0
});

const pokesSearchKeywordAtom = atom({
  key: "app/pokesSearchKeyword",
  default: ""
});

function PokeListPage() {

  const [pokes, setPokes] = useRecoilState(pokesAtom); //useState([]);
  const [offset, setOffset] =  useRecoilState(pokesOffsetAtom); //useState(0);
  const [searchKeyword, setSearchKeyword] = useRecoilState(
    pokesSearchKeywordAtom
  );


  const totalItems = 5;
  const maxItemsInAPage = 2;
  const limit =
    offset + maxItemsInAPage < totalItems
      ? maxItemsInAPage
      : totalItems - offset;

  // const { isLoading, error, data } = useQuery("pokeList", () =>
  //   fetch("http://127.0.0.1:8000/product/admin").then((res) => res.json())
  // );
 const {
    isLoading,
    error,
    data
  } = useQuery(`pokemon?offset=${offset}&limit=${limit}`,
     async () =>
         axiosInstance.get(`product/asdf?offset=${offset}&limit=${limit}`)
    // fetch(
    //   `http://127.0.0.1:8000/product/asdf?offset=${offset}&limit=${limit}`
    // )
        .then((res) =>
            res.data
            //res.json()
            )
  );


  if (isLoading) return "Loading...";
  if (error) return "An error has occurred: " + error.message;

  console.log("asdfasdfasdf");
  console.log(data);


  if ( offset + limit > pokes.length ) {
    setPokes([...pokes, ...data.results]);
  }

  const showMore = () => {
    console.log("shorMore!");
    setOffset(offset + limit);
  };
  const showPrev = () => {
    setOffset(offset - maxItemsInAPage);
  };

  const btnShowPrevVisible = offset > 0;

  const btnShowMoreVisible = offset + limit < totalItems;

  const filteredPokes =
    searchKeyword.length === 0
      ? pokes
      : pokes.filter((poke) => poke.product_name.includes(searchKeyword));




  return (
    <>
       <h1 className="py-2 px-2 flex font-bold bg-gray-500 sticky top-0">
        <span className="text-white">관리자 상품 리스트</span>
        <div className="flex-grow" />
         <input
          type="search"
          placeholder="검색"
          className="input input-bordered input-xs"
          onChange={(e) => setSearchKeyword(e.target.value)}
          value={searchKeyword}
        />
      </h1>

      <ul>
        {filteredPokes.map((poke) => {
          const no = poke.id;

          return (
            <li key={poke.id} className="hover:bg-gray-100">
              <Link to={"poke?id=" + poke.id} className="flex items-center">
                <img
                  src={poke.imgs[0].img_url}
                />
                <div className="ml-2">
                  <h2 className="w-20">
                    <span className="badge badge-outline badge-primary">
                      {no}
                    </span>
                  </h2>
                  <h2>{poke.name}</h2>
                    <div className="ml-2">
                        <h1 key={poke.id} className="flex items-center">{poke.product_name}</h1>
                           <p className="badge badge-outline badge-primary">{poke.description}</p>
                           <strong>가격 👀 {poke.price}</strong>{' '}
                           <strong>재고 ✨ {poke.stock}</strong>{' '}
                           <strong>등록날짜 : {poke.register_date}</strong>{' '}
                           <strong>상태 :  {poke.status}</strong>{' '}
                           <strong>shop: {poke.shop}</strong>
                      </div>

                </div>

              </Link>

            </li>

          );
        })}
      </ul>
     {/*    <div>*/}
     {/*  {mutation.isLoading ? (*/}
     {/*    'Adding todo...'*/}
     {/*  ) : (*/}
     {/*    <>*/}
     {/*      {mutation.isError ? (*/}
     {/*        <div>An error occurred: {mutation.error.message}</div>*/}
     {/*      ) : null}*/}

     {/*      {mutation.isSuccess ? <div>Todo added!</div> : null}*/}

     {/*      <button*/}
     {/*        onClick={() => {*/}
     {/*          mutation.mutate({ id: new Date(), title: 'Do Laundry' })*/}
     {/*        }}*/}
     {/*      >*/}
     {/*        Create Todo*/}
     {/*      </button>*/}
     {/*    </>*/}
     {/*  )}*/}
     {/*</div>*/}
      {/*  <div className="px-2">*/}
      {/*  {btnShowPrevVisible ? (*/}
      {/*    <button onClick={showPrev} className="btn btn-block btn-secondary">*/}
      {/*      이전*/}
      {/*    </button>*/}
      {/*  ) : (*/}
      {/*    <button className="btn btn-block btn-disabled">*/}
      {/*      첫 페이지 입니다.*/}
      {/*    </button>*/}
      {/*  )}*/}
      {/*</div>*/}

      <div className="px-2 mt-2">
        {btnShowMoreVisible ? (
          <button
            onClick={showMore}
            className={classnames("btn", "btn-block", "btn-secondary", {
              loading: isLoading
            })}
          >
            More
          </button>
        ) : (
          <button className="btn btn-block btn-disabled">
            마지막 페이지 입니다.
          </button>
        )}
      </div>
    </>
  );
};




const baseURL = 'http://127.0.0.1:8000/';

const axiosInstance = axios.create({
	baseURL: baseURL,
	timeout: 5000,
	headers: {
		'Authorization': localStorage.getItem('access_token')
			? 'Bearer ' + localStorage.getItem('access_token')
			: null,
		'Content-Type': 'application/json',
		accept: 'application/json',
	},
});

axiosInstance.interceptors.response.use(
	(response) => {
		return response;
	},
	async function (error) {
		const originalRequest = error.config;

		if (typeof error.response === 'undefined') {
			alert(
				'A server/network error occurred. ' +
					'Looks like CORS might be the problem. ' +
					'Sorry about this - we will get it fixed shortly.'
			);
			return Promise.reject(error);
		}

		// if (
		// 	error.response.status === 401 &&
		// 	originalRequest.url === baseURL + 'api/token/refresh/'
		// ) {
		// 	window.location.href = '/login/';
		// 	return Promise.reject(error);
		// }

		if (
			error.response.data.code === 'token_not_valid' &&
			error.response.status === 401
		) {
		    console.log("asdfasdfasdf");
			const refreshToken = localStorage.getItem('refresh_token');
		    console.log(refreshToken);

			if (refreshToken) {
				const tokenParts = JSON.parse(atob(refreshToken.split('.')[1]));

				// exp date in token is expressed in seconds, while now() returns milliseconds:
				const now = Math.ceil(Date.now() / 1000);
				console.log(tokenParts.exp);

				if (tokenParts.exp > now) {
					return axiosInstance
						.post('api/token/refresh/', { refresh: refreshToken })
						.then((response) => {
							localStorage.setItem('access_token', response.data.access);
							// localStorage.setItem('refresh_token', response.data.refresh);

							axiosInstance.defaults.headers['Authorization'] =
								'Bearer ' + response.data.access;
							originalRequest.headers['Authorization'] =
								'Bearer ' + response.data.access;

							return axiosInstance(originalRequest);
						})
						.catch((err) => {
							console.log(err);
						});
				} else {
					console.log('Refresh token is expired', tokenParts.exp, now);
					window.location.href = '/loginsdf/';
				}
			} else {
				console.log('Refresh token not available.');
				window.location.href = '/loginsdf/';
			}
		}

		// specific error handling done elsewhere
		return Promise.reject(error);
	}
);


const LoginTestPage = () => {
    const [appState, setAppState] = useState({
		loading: true,
		posts: null,
	});
    const [success, setSuccess] = useState("");

    useEffect(() => {
		axiosInstance.get("user/login/test").then((res) => {
		    // console.log(res);
			// const allPosts = res.data;
			// setAppState({ loading: false, posts: allPosts });
			// console.log(res.data);
			return JSON.stringify(res.data.Success);
		}).then(data => {
		setSuccess(data);
    })
	}, []);

	return (
	    <>
		<div className="App">
			<h1>Latest Posts</h1>
		</div>
         {!success ? <div>Loading...</div>:<div>{ success }</div>}
        </>
	);
	};



const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (localStorage.getItem('token') !== null) {
      window.location.replace('http://localhost:3000/');
    } else {
      setLoading(false);
    }
  }, []);

  const onSubmit = e => {
    e.preventDefault();

    const user = {
      username: email,
      password: password
    };
    console.log(JSON.stringify(user));

    fetch('http://127.0.0.1:8000/user/lioncustomlogin', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(user)
    })
      .then(res => res.json())
      .then(data => {
        if (data.status === 403) {
            alert(
				'아이디 비밀번호 확인하세요'
			);
            window.location.href = '#/loginsdf/';
        }
        if (data.status === 401 && data.code==="token_not_valid") {
            alert(
				'토큰만료'
			);

        }
        if (data.status === 201) {
            alert(
				'어서오세요 '
			);
          localStorage.clear();
          localStorage.setItem('access_token', data.access);
          localStorage.setItem('refresh_token', data.refresh);

          window.location.replace('http://localhost:3000/');
        } else {
          setEmail('');
          setPassword('');
          localStorage.clear();
          setErrors(true);
        }
      });
  };

    const style = {
        marginTop: "20px",
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
        };
  return (
    <div style={style}>
        관리자 로그인 페이지
      {loading === false && <h1>Login</h1>}
      {errors === true && <h2>Cannot log in with provided credentials</h2>}
      {loading === false && (
        <form onSubmit={onSubmit}>
          <label htmlFor='email'>Email address:</label> <br />
          <input
            name='email'
            type='email'
            value={email}
            required
            onChange={e => setEmail(e.target.value)}
          />{' '}
          <br />
          <label htmlFor='password'>Password:</label> <br />
          <input
            name='password'
            type='password'
            value={password}
            required
            onChange={e => setPassword(e.target.value)}
          />{' '}
          <br />
          <input type='submit' value='Login' />
        </form>
      )}
    </div>
  );
};

const App = () => {
  return (
    <RecoilRoot>
      <QueryClientProvider client={queryClient}>
        <Router>
          <Switch>
            <Route path="/logintest" component={LoginTestPage} />

            <Route path="/loginsdf" component={LoginPage} />

            <Route path="/poke" component={PokeDetailPage} />
            <Route path="/" component={PokeListPage} />

          </Switch>
        </Router>
      </QueryClientProvider>
    </RecoilRoot>
  );
};



ReactDOM.render(<App />, document.getElementById("root"));
//export default App;
