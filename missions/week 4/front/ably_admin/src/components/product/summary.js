import { useState, useEffect } from 'react';
import axios from 'axios';
import axiosInstance from '../utils/AxiosInstance';
import { useNavigate } from 'react-router-dom';
import CustomizedDialogs from './test'

import * as React from 'react';
import PropTypes from 'prop-types';
import Button from '@mui/material/Button';
import Avatar from '@mui/material/Avatar';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import ListItemText from '@mui/material/ListItemText';
import DialogTitle from '@mui/material/DialogTitle';
import Box from '@mui/material/Box';
import Dialog from '@mui/material/Dialog';
// import PersonIcon from '@mui/icons-material/Person';
// import AddIcon from '@mui/icons-material/Add';
import Typography from '@mui/material/Typography';
// import { makeStyles } from '@material-ui/core/styles';




function SimpleDialog(props) {
    const { onClose, selectedValue, open } = props;

    console.log('test&', selectedValue);

    const handleClose = () => {
        onClose();
    };

    // const handleListItemClick = (value) => {
    //   onClose(value);
    // };

    // const useStyles = makeStyles(() => ({
    //     box: { width: "800px" },
    // }));

    return (
        //   <Dialog classes={{ paper: classes.box }} onClose={handleClose} open={open}>
        <Dialog maxWidth="md" onClose={handleClose} open={open}>
            <div style={{ fontSize:30 }}>{selectedValue.name} 세부사항</div>

            <div className='flex justify-start'>
                <div className='w-2/4 '>
                    <img src={`http://localhost:8000`+selectedValue.image} />
                </div>
                <div className='w-2/4'>
                    가격?{selectedValue.price}
                    <br/>
                    실제가격?{selectedValue.sale_price}
                    <br/>
                    등록시각?{selectedValue.reg_date}
                    <br/>
                    수정시각?{selectedValue.update_date}
                    <br/>
                    숨김여부?{`${selectedValue.is_hidden}`}
                    <br/>
                    삭제여부?{`${selectedValue.is_deleted}`}
                    <br/>
                    조회수?{`${selectedValue.hit_count}`}
                    <br/>
                    설명?{selectedValue.description}
                    <br/>
                    좋아요 수?{`${selectedValue.like_count}`}
                    <br/>
                    

                </div>
            </div>

            {/* <Box
            sx={{
                width: '1000px',
                display: 'flex',
                flexDirection: 'column',
                m: 'auto',
            }}
        >


        </Box> */}

            {/* <List sx={{ pt: 0 }}>
          {emails.map((email) => (
            <ListItem button onClick={() => handleListItemClick(email)} key={email}>
              <ListItemAvatar>
                <Avatar sx={{ bgcolor: blue[100], color: blue[600] }}>
                </Avatar>
              </ListItemAvatar>
              <ListItemText primary={email} />
            </ListItem>
          ))}
  
          <ListItem autoFocus button onClick={() => handleListItemClick('addAccount')}>
            <ListItemAvatar>
              <Avatar>
              </Avatar>
            </ListItemAvatar>
            <ListItemText primary="Add account" />
          </ListItem>
        </List> */}
        </Dialog>
    );
}

SimpleDialog.propTypes = {
    onClose: PropTypes.func.isRequired,
    open: PropTypes.bool.isRequired,
    selectedValue: PropTypes.object.isRequired,
};














const ProductSummary = (props) => {
    const [open, setOpen] = React.useState(false);
    const [selectedValue, setSelectedValue] = React.useState({});

    const handleClickOpen = () => {
        setOpen(true);
        // props.is_deleted = JSON.stringify(props.is_deleted)
        setSelectedValue(props.product);
    };

    const handleClose = (value) => {
        setOpen(false);
    };

    const navigate = useNavigate()
    const onClickDelete = (productId) => {

        if (window.confirm("삭제할까요??")) {
            const url = 'http://127.0.0.1:8000/api/product/' + productId
            axiosInstance.delete(url)
            alert("삭제되었습니다.");
        }
    }
    // const temp = (props) =>{
    //     console.log("console test")
    //     console.log(props)
    //     return (
    //         <CustomizedDialogs/>
    //     )

    // }



    return (
        <tr className='App'>

            <td>{props.id}</td>
            <td className="w-1/4"><img className="w-3/4" src={props.image_url} onClick={handleClickOpen} href="/" /></td>
            <td>{props.name}</td>
            <td>{props.description}</td>
            <td>{props.reg_date}</td>
            <td> <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" onClick={() => onClickDelete(props.id)} type="button">
                삭제
            </button>
            </td>
            <SimpleDialog
                selectedValue={selectedValue}
                open={open}
                onClose={handleClose}
            />
        </tr>
    )
}

export default ProductSummary;