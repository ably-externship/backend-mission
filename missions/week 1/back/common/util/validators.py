import re

from common.exception.EmailValidException import EmailValidException
from common.exception.PhoneNumberValidException import PhoneNumberValidException


def validate_email(value):
    email_regex = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    email_validation = email_regex.match(value)
    if email_validation:
        return True
    else:
        raise EmailValidException()

def validate_phone(value):
    phone_regex = re.compile('\d{3}-\d{3,4}-\d{4}')
    phone_validation = phone_regex.match(value)
    if phone_validation:
        return True
    else:
        raise PhoneNumberValidException()


