class PhoneNumberValidException(Exception):
    def __init__(self):
        self.msg = "휴대전화 번호 형식에 맞지 않습니다."

    def __str__(self):
        return "휴대전화 번호 형식에 맞지 않습니다."