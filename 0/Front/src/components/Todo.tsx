import { Card, Button } from 'antd';
import Axios from 'axios';

export default function Todo( props: any) {

    const { todo } = props;
    const { task, id } = todo;

    function delTodo() {

        Axios.delete('http://localhost:8000/app/' + id)
        .then(

            (response) => {

                if ( response.status === 204 ) {
                    window.location.reload();
                }

            }

        )
        .catch(

            (error) => {
                console.log(error);
            }

    )
    }
    

    return (
        <Card>
            <Button style={{marginRight: 5}} size='small'>
                {id}
            </Button>
            {task}
            <Button type="primary" danger style={{marginLeft: 15}} onClick={ delTodo } size='small'>
                -
            </Button>
        </Card>
    );

}