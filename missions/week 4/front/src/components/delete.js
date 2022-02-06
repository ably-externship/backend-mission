import React, { useState, useEffect } from 'react';
import axiosInstance from '../axios';
import { useNavigate, useParams } from 'react-router-dom';
//MaterialUI
import Container from '@material-ui/core/Container';
import Button from '@material-ui/core/Button';
import Box from '@material-ui/core/Box';

export default function Delete() {
	const navigate = useNavigate();
	const { id } = useParams();

	const handleSubmit = (e) => {
		e.preventDefault();
		axiosInstance
			.delete('seller/' + id)
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
			<Container component="main" maxWidth="sm">
				<Box
					display="flex"
					justifyContent="center"
					m={1}
					p={1}
					bgcolor="background.paper"
				>
					<Button
						variant="contained"
						color="secondary"
						type="submit"
						onClick={handleSubmit}
					>
						Press here to confirm delete
					</Button>
				</Box>
			</Container>
		);
	}
}