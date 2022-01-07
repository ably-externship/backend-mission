import re

from django.core.exceptions import ValidationError

REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEX_PASSWORD = '^[a-zA-Z0-9!@#$%^&*+=_]{8,12}$'
REGEX_PHONE_NUMBER = '^01[0-9]{8,9}$'
REGEX_NAME = '^[a-zA-Z가-힣]{1,20}$'

def validate_email(email):
    if not re.match(REGEX_EMAIL, email) or email is None:
        raise ValidationError('Invalid Email')

def validate_password(password):
    if not re.match(REGEX_PASSWORD, password) or password is None:
        raise ValidationError('Invalid Password')

def validate_phone_number(phone_number):
    if not re.match(REGEX_PHONE_NUMBER, phone_number) or phone_number is None:
        raise ValidationError('Invalid Phone Number')

def validate_name(name):
    if not re.match(REGEX_NAME, name) or name is None:
        raise ValidationError('Invalid Name')