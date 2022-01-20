class EmailValidException(Exception):
    def __init__(self):
        self.msg = "이메일 형식에 맞지 않습니다."

    def __str__(self):
        return "이메일 형식에 맞지 않습니다."