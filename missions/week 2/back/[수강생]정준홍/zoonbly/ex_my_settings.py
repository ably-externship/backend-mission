# MySQL 연동하기
# my_settings.py 라는 파일 생성하여 밑의 코드 작성.
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql', #사용할 엔진 설정
        'NAME' : 'database name', # 사용할 데이터베이스 이름 
        'USER' : 'user name', # MySQL DB 접속 계정명
        'PASSWORD' : 'password', # 해당 DB 접속 비밀번호
        'HOST' : 'DB address', # 실제 DB 주소 ex) local host
        'PORT' : 'port number', # 포트번호
    }
}
SECRET_KEY = '기존 settings.py의 django 시크릿키 입력'