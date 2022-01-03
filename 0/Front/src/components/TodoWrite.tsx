import React from 'react';
import { Form, Input, Button } from 'antd';
import Axios from 'axios';

export default function TodoWrite() {

    const onFinish = ( values: any ) => {

        async function fn() {

            const { task } = values;

            const data = {
                task,
            }

            console.log(data);

            try {

                const response = await Axios.post(
                    'http://localhost:8000/app/',
                    data
                );

                if ( response.status === 201 ) {
                    window.location.reload();
                }

            } catch (error: any) {
                console.log(error);
            }


        }
        fn();
    }
    

    return (
        <Form onFinish={onFinish} style={{display: "flex", flexDirection: "row"}} >
            <Form.Item  name="task"  >
                <Input showCount maxLength={100} style={{ width:500 }} />
            </Form.Item>
            <Form.Item>
                <Button type="primary"  htmlType="submit" style={{marginLeft: 35}}> + </Button>
            </Form.Item>
        </Form>
    )

}