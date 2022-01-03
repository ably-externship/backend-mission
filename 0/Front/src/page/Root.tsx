import React, { useEffect, useState } from 'react';
import { Layout, Menu } from 'antd';
import Axios from 'axios';
import Todo from '../components/Todo';
import TodoWrite from '../components/TodoWrite';


export default function Root() {

    const [ todoList, setTodoList ] = useState([]);

    useEffect( () => {

        Axios.get('http://localhost:8000/app/')
        .then(

            (response) => {

                const { data } = response;

                setTodoList(data);

            }

        )
        .catch(

            (error) => {
                console.log(error);
            }

        );

    }, [] );

    const { Header, Content, Footer } = Layout;


    return (
        <Layout className="layout">
            <Header>
            <Menu theme="dark" mode="horizontal">
                <Menu.Item>
                    홈
                </Menu.Item>
            </Menu>
            </Header>
            <Content style={{ padding: '0 50px' }}>
                <div className="site-layout-content" style={{ marginTop:50 }}>
                    <TodoWrite />
                    {
                        todoList.map(
                            (todo: any) => {
                                return <Todo todo={todo} key={todo.id} />;
                            }
                        )
                    }
                </div>  
            </Content>
            <Footer style={{ textAlign: 'center' }}>
                Copyright 2022. dnlwjtud All Rights Reserved.
            </Footer>
        </Layout>
    );

}