### 파이썬 패키지 설치
```bash
pip install -U -r requirements.txt
```
### 로컬 mysql 데이터베이스 셋업
```bash
docker-compose up -d
```

### DB 마이그레이션

> 설계된 모델에 대한 스키마를 데이터베이스에 반영

```bash
python manage.py migrate
```

### 서버실행

```bash
python manage.py runserver
```