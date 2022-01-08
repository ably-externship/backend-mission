from django import forms
from django.contrib.auth.hashers import check_password, make_password
from .models import User

class RegisterForm(forms.Form):
	email = forms.EmailField(
		error_messages={
			'required': 'E-Mail을 입력해주세요'
		}, max_length=64, label='이메일'
	)
	password = forms.CharField(
		error_messages={
			'required': '비밀번호를 입력해주세요'
		}, widget=forms.PasswordInput(), label='Password'
	)
	re_password = forms.CharField(
				error_messages={
			'required': '비밀번호를 입력해주세요'
		}, widget=forms.PasswordInput(), label='Password 확인'
	)

	def valid(self):
		valid_data = super.clean()
		email = valid_data.get('email')
		password = valid_data.get('password')
		re_password = valid_data.get('re_password')

		if password and re_password:
			if password != re_password:
				self.add_error('password', '비밀번호가 서로 다릅니다')
				self.add_error('re_password', '비밀번호가 서로 다릅니다')
			else:
				user = User(
					email=email,
					password=make_password(password),
				)
				user.save()


class LoginForm(forms.Form):
	email = forms.EmailField(
		error_messages={
			'required': 'E-Mail을 입력해주세요'
		}, max_length=64, label='이메일'
	)
	password = forms.CharField(
		error_messages={
			'required': '비밀번호를 입력해주세요'
		}, widget=forms.PasswordInput(), label='Password'
	)

	def valid(self):
		valid_data = super.clean()
		email = valid_data.get('email')
		password = valid_data.get('password')

		if email and password:
			try:
				user = User.objects.get(email=email)
			except User.DoesNotExist:
				self.add_error('email','존재하지 않는 이메일입니다!')

			if not check_password(password, user.password):
				self.add_error('password', '비밀번호를 틀렸습니다.')
			else:
				self.email = user.email
