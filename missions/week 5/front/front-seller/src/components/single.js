import React, { useState, useEffect } from 'react';
import axiosInstance from '../axios';
import { useNavigate, useParams } from 'react-router-dom';
import Products from './products';
import ProductLoadingConponent from './productLoading';

//MaterialUI
import CardMedia from '@material-ui/core/CardMedia';
import CssBaseline from '@material-ui/core/CssBaseline';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import DeleteForeverIcon from '@material-ui/icons/DeleteForever';
import Link from '@material-ui/core/Link';

const useStyles = makeStyles((theme) => ({
	cardMedia: {
		paddingTop: '100%', // 16:9
	},
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
	},
}));

export default function Product() {
	const navigate = useNavigate();
	const ProductLoading = ProductLoadingConponent(Products);
	const [appState, setAppState] = useState({
		loading: false,
		products: null,
	});


	const { id } = useParams();
	const classes = useStyles();

	const [data, setData] = useState({ products: [] });

	useEffect(() => {
		axiosInstance.get('seller/' + id).then((res) => {
			setData({ products: res.data });
			console.log(res.data);
		});
	}, [setData]);



	const handleSubmit = (e) => {
		e.preventDefault();
		axiosInstance
			.delete('seller/'+ data.products.id)
			.catch(function (error) {
				if (error.response) {
					console.log(error.response.data);
					console.log(error.response.status);
					console.log(error.response.headers);
				}
			})
			.then(function () {
					navigate('/');
			});
	};

	if (localStorage.getItem('access_token')== null) {
		return (
			<div className="App">
				<h1>로그인해주세요.</h1>
			</div>
		);
	} else {

		return (
			<Container component="main" maxWidth="md">
				<CssBaseline />
				<div className={classes.paper}></div>
				<div className={classes.heroContent}>
					<Container maxWidth="sm">
						<CardMedia
							className={classes.cardMedia}
							image={data.products.image_url}
							title="Image title"
						/>
						<Typography
							component="h1"
							variant="h2"
							align="center"
							color="textPrimary"
							gutterBottom
						>
							{data.products.name}
						</Typography>
						<Typography
							variant="h5"
							align="center"
							color="textSecondary"
							paragraph
						>
							{data.products.description}
						</Typography>
						<Typography
							variant="h5"
							align="center"
							color="textSecondary"
							paragraph
						>
							{data.products.price}원
						</Typography>
						<Button
						variant="contained"
						color="secondary"
						type="submit"
						onClick={handleSubmit}
						>
							상품 삭제하기
						</Button>
					</Container>
				</div>
			</Container>
		);
	}
}