import React, {useEffect, useState} from 'react';
import axios from "axios";
import {useHistory} from "react-router-dom";

function KeywordRegister(props) {

    const history = useHistory();
    const [keywordList, setKeywordList] = useState([]);
    const [keyword1, setKeyword1] = useState('');
    const [keyword2, setKeyword2] = useState('');
    const [keyword3, setKeyword3] = useState('');


    useEffect(() => {
        const take = async () => {
            const {data} = await axios.get('http://127.0.0.1:8000/user/recommand/',
                {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`,
                    }
                }
            );
            setKeywordList(data);
        };
        take();
    }, []);


    const Addkeyword = async ()=> {


        const inputValue = {keyword1: keyword1, keyword2: keyword2, keyword3:keyword3};
        const find = async () => {
            await axios.patch('http://127.0.0.1:8000/user/recommand/create/', inputValue,
                {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`,
                    }
                }).then(

            )
        }
        find()
        alert('키워드 추가 완료')
        history.push('/');
    };



    return (
        <>
            <div className="signUp">
                <div>
                    <h1 className="menu">키워드 등록 화면</h1>
                    {/*<span>{JoinLoign}</span>*/}
                    <form className="">
                        {
                            keywordList && keywordList.map((key) =>
                            <div key={key.id}>
                                <input type="text" onChange={e => setKeyword1(e.target.value)} defaultValue={key.keyword1} placeholder="키워드1를 입력하세요" className="signUpInput"/>
                                <input type="text" onChange={e => setKeyword2(e.target.value)} defaultValue={key.keyword2} placeholder="키워드2를 입력하세요" className="signUpInput"/>
                                <input type="text" onChange={e => setKeyword3(e.target.value)} defaultValue={key.keyword3} placeholder="키워드3를 입력하세요" className="signUpInput"/>
                            </div>

                            )
                        }
                        <button onClick={Addkeyword} className="signUpButton">등록하기</button>
                    </form>
                </div>
            </div>
        </>
    );
}

export default KeywordRegister;