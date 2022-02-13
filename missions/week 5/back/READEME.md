# Mutbly-Shoppingmall API

### 필요
- Python 3.9.x
- Docker

## 서버 구동 방법

### 로컬환경 서버 구동

1. 파이썬 패키지 설치
```bash
pip install -U -r requirements.txt
```
2. 로컬 mysql 데이터베이스 셋업
```bash
docker-compose up -d
```

3. DB 마이그레이션

> 설계된 모델에 대한 스키마를 데이터베이스에 반영

```bash
python manage.py migrate
```

4. 서버실행

```bash
python manage.py runserver
```

5. 서버 정상 구동 확인

웹 브라우저에서 http://127.0.0.1:8000/ 로 접속하여 페이지가 나온다면 정상적으로 서버 구동 완료.



## API Specifications
### 회원가입
[요청]
- URL: POST /api/accounts/signup/
- Body
```bash
{
  "username": "test",
  "email": "test@test.com",
  "password": "1234"
} 
```
[응답]
- Body
```bash
{
  "username": "test",
  "email": "test@test.com",
  "password": "1234"
} 
```
- Error

|에러코드|설명|
|------|-----|
|400| 중복된 username이 입력된 경우|
|401| 파라미터 입력이 잘못된 경우|

### 로그인
[요청]
- URL: POST /api/accounts/login/
- Body
```bash
{
  "username": "test",
  "password": "1234"
} 
```
[응답]
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200

- Error

|에러코드|설명|
|------|-----|
|400| 등록된 user가 없는 경우|
|401| Username or Password 틀릴 경우|

### 로그아웃
[요청]
- URL: POST /api/accounts/logout/
- Body
```bash
{
  "username": "test",
  "password": "1234"
} 
```
[응답]
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200

### 비밀번호 변경
[요청]
- ###### URL: PUT _/api/accounts/change-password/:pk/_
  - Path 파라미터 설명: pk는 change-password의 식별 아이디를 입력합니다.
- Body
```bash
{
  "password": "test",
  "password2": "test"
  "current_password":"CurrentPassword"
} 
```
[응답]
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200

- Error

|에러코드|설명|
|------|-----|
|400| 변경하는 비밀번호, 기존 비밀번호가 틀린 경우|

  
### 상품 조회
[요청]
- URL: GET /api/products/

[응답]
- Body
```bash
{
        "id": 7,
        "name": "워커",
        "author_id": 4,
        "seller": "워커나라",
        "price": 5,
        "image": "http://127.0.0.1:8000/media/product/woker_DxwdMCK.jpg",
        "description": "멋있는 워커",
        "product_option": [
            {
                "id": 9,
                "size": "250",
                "color": "brown",
                "stock_count": 2,
                "product_id": 7
            }
        ]
    },
    {
        "id": 10,
        "name": "원피스",
        "author_id": 1,
        "seller": "늑대",
        "price": 80000,
        "image": "http://127.0.0.1:8000/media/product/onepice2_KVyRT2K.jpg",
        "description": "봄용 원피스",
        "product_option": []
    },
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명
    - 관리자,고객이면 모든 상품 목록들의 결과가 반환됩니다.
    - 입점사 이면 본인이 등록한 상품 목록들의 결과만 반환됩니다.

- Error

|에러코드|설명|
|------|-----|
|404| 상품 목록이 없는 경우|

### 상품 등록
[요청]
- URL: POST /api/products/
  
```bash
{
        "name": "드레스",
        "seller": "여우몰",
        "price": 22000,
        "image": "http://127.0.0.1:8000/media/product/dress_red_IHq6vEU.jpg",
        "description": "박시하고 이쁨",    
} 
```
- Body 파라미터 설명
  - 관리자 or 입점사만 등록 가능합니다.
    - name : 상품 이름을 의미합니다. 문자열을 입력합니다.
    - seller : 입점사 이름을 의미합니다. 문자열을 입력합니다.
    - price : 상품가격을 의미합니다. 0 이상의 정수로만 입력해야 합니다.
    - image : 사진을 의미합니다. 사진 파일을 업로드 합니다.
    - description : 상품 설명을 의미합니다. 문자열을 입력합니다.

[응답]
- Body
```bash
{
    "id": 15,
    "name": "드레스",
    "author_id": 1,
    "seller": "여우몰",
    "price": 22000,
    "image": "/media/product/trainning_XpWd0Q3.jpg",
    "description": "박시하고 이쁨",
    "product_option": []
}
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명
    - 관리자,고객이면 모든 상품 목록들의 결과가 반환됩니다.
    - 입점사 이면 본인이 등록한 상품 목록들의 결과가 반환됩니다.

- Error

|에러코드|설명|
|------|-----|
|404| 상품 목록이 없는 경우|

### 상품 상세 조회
[요청]
- URL: GET /api/products/:pk/
  - Path 파라미터 설명 : pk는 products의 식별 아이디를 입력합니다.
  
[응답]
- Body
```bash
{
        "id": 1,
        "name": "드레스",
        "author_id": 1,
        "seller": "여우몰",
        "price": 22000,
        "image": "http://127.0.0.1:8000/media/product/dress_red_IHq6vEU.jpg",
        "description": "박시하고 이쁨",
        "product_option": [
            {
                "id": 1,
                "size": "44",
                "color": "red",
                "stock_count": 4,
                "product_id": 1
            },
            {
                "id": 2,
                "size": "44",
                "color": "green",
                "stock_count": 46,
                "product_id": 1
            },
            {
                "id": 3,
                "size": "44",
                "color": "blue",
                "stock_count": 6,
                "product_id": 1
            }
}
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명 : 상품 상세 조회된 결과가 반환됩니다.

- Error

|에러코드|설명|
|------|-----|
|404| 상품 목록이 없는 경우|

### 상품 수정
[요청]
- URL: PATCH /api/products/:pk/
  - Path 파라미터 설명 : pk는 products의 식별 아이디를 입력합니다.
- Body
```bash
{
    "price":10000
}
```
- Body 파라미터 설명
    - price : 상품가격을 의미합니다. 0 이상의 정수로만 입력해야 합니다.
    
[응답]
- Body
```bash
{
    "id": 1,
    "name": "드레스",
    "author_id": 1,
    "seller": "여우몰",
    "price": 10000,
    "image": "http://127.0.0.1:8000/media/product/dress_red_IHq6vEU.jpg",
    "description": "박시하고 이쁨",
    "product_option": [
        {
            "id": 1,
            "size": "44",
            "color": "red",
            "stock_count": 4,
            "product_id": 1
        }
}
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명  : 상품 수정된 결과가 반환됩니다.

- Error

|에러코드|설명|
|------|-----|
|400| 상품 목록이 없는 경우|

### 상품 삭제
[요청]
- URL: DELETE /api/products/:pk/
  - Path 파라미터 설명 : pk는 products의 식별 아이디를 입력합니다.

[응답]
- Body
```bash
{
  HTTP 204 No Content
}
```
- 응답에 대한 설명
  - 응답 Body 설명  : 내역이 삭제 됩니다.

### 장바구니 조회
[요청]
- URL: GET /api/products/cart/items/

[응답]
- Body
```bash
{
    {
        "quantity": 20,
        "product_name": "워커",
        "product_option_size": "250",
        "product_option_color": "brown"
    },
    {
        "quantity": 1,
        "product_name": "워커",
        "product_option_size": "250",
        "product_option_color": "brown"
    }
}
```
- Body 파라미터 설명
    - quantity : 상품 수량을 의미 합니다.
    - product_name : 상품 이름을 의미합니다.
    - product_option_size : 상품 크기를 의미합니다.
    - product_option_color : 상품 색상을 의미합니다.

- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명
    - 로그인한 user의 장바구니 목록 결과가 반환됩니다.

- Error

|에러코드|설명|
|------|-----|
|404| 장바구니 목록이 없는 경우|

### 장바구니 등록
[요청]
- URL: POST /api/products/cart/items/


- Body
```bash
{
        "quantity": 10,
        "product_id": 1,
        "user_id": 1,
        "product_option_id": 2
}
```
- Body 파라미터 설명
  - quantity : 상품 수량을 의미합니다.
  - product_id : 상품을 의미합니다.
  - user_id : 고객을 의미합니다.
  - product_option_id : 상품 옵션을 의미합니다.

[응답]
- Body
```bash
{
    "id": 14,
    "quantity": 10,
    "product_id": 1,
    "user_id": 1,
    "product_option_id": 2,
    "product_name": "드레스",
    "product_option_size": "44",
    "product_option_color": "green"
}
```
- Body 파라미터 설명
  - quantity : 상품 수량을 의미 합니다.
  - product_id : 상품을 의미합니다.
  - user_id : 고객을 의미합니다.
  - product_option_id : 상품 옵션을 의미합니다.
  - product_name : 상품 이름을 의미합니다.
  - product_option_size : 상품 크기를 의미합니다.
  - product_option_color : 상품 색상을 의미합니다.
  

- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 201
  - 응답 Body 설명 : 장바구니가 생성된 결과가 반환됩니다.


- Error

|에러코드|설명|
|------|-----|
|400| 파라미터 입력이 잘못된 경우|

### 장바구니 상세 조회
[요청]
- URL: GET /api/products/cart/items/:pk/
  - Path 파라미터 설명 : pk는 items의 식별 아이디를 입력합니다.

[응답]
- Body
```bash
{
    "id": 1,
    "quantity": 20,
    "product_id": 7,
    "user_id": 1,
    "product_option_id": 9,
    "product_name": "워커",
    "product_option_size": "250",
    "product_option_color": "brown"
}
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명 : 장바구니 상세 조회된 결과가 반환됩니다.

- Error

|에러코드|설명|
|------|-----|
|404| 장바구니 상품이 없는 경우|

### 장바구니 상품 수정
[요청]
- URL: PATCH /api/products/cart/items/:pk/
  - Path 파라미터 설명 : pk는 items의 식별 아이디를 입력합니다.
- Body
```bash
{
  "quantity": 50
}
```
- Body 파라미터 설명
  - quantity : 상품수량을 의미합니다. 0 이상의 정수로만 입력해야 합니다.

[응답]
- Body
```bash
{
    "id": 1,
    "quantity": 50,
    "product_id": 7,
    "user_id": 1,
    "product_option_id": 9,
    "product_name": "워커",
    "product_option_size": "250",
    "product_option_color": "brown"
}
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명  : 장바구니 상품 수정된 결과가 반환됩니다.

- Error

|에러코드|설명|
|------|-----|
|400| 파라미터 입력이 잘못된 경우|

### 장바구니 삭제
[요청]
- URL: DELETE /api/products/cart/items/:pk/
  - Path 파라미터 설명 : pk는 items의 식별 아이디를 입력합니다.

[응답]
- Body
```bash
{
  HTTP 204 No Content
}
```
- 응답에 대한 설명
  - 응답 Body 설명  : 내역이 삭제 됩니다.

### 장바구니 상품 주문
[요청]
- URL: POST /api/products/cart/item/orders/


- Body
```bash
{
    "orders":[
        { "quantity":100,  "user_id":1, "product_id":7, "product_option_id":9},
        { "quantity":1, "user_id":1, "product_id":7, "product_option_id":9},
        { "quantity":5, "user_id":1, "product_id":7, "product_option_id":9},
        { "quantity":10, "user_id":1, "product_id":1, "product_option_id":1}
    ]
}
```
- Body 파라미터 설명
  - orders : 장바구니에 담겨 있는 상품 리스트를 의미합니다.
  - quantity : 상품 수량을 의미합니다.
  - user_id : 고객을 의미합니다.
  - product_id : 상품을 의미합니다.
  - product_option_id : 상품 옵션을 의미합니다.

[응답]
- Body
```bash
{
    "orders": [
        {
            "quantity": 100
        },
        {
            "quantity": 1
        },
        {
            "quantity": 5
        },
        {
            "quantity": 10
        }
    ]
}
```
- Body 파라미터 설명이
    - quantity : 상품 수량을 의미 합니다.

- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 201
  - 응답 Body 설명 : 주문된 결과가 반환됩니다.


- Error

|에러코드|설명|
|------|-----|
|400| 파라미터 입력이 잘못된 경우|


### 주문 조회
[요청]
- URL: GET /api/products/order/items/

[응답]
- Body
```bash
[
    {
        "id": 6,
        "quantity": 10,
        "user_id": 1,
        "product_id": 1,
        "product_option_id": 2
    },
    {
        "id": 7,
        "quantity": 2,
        "user_id": 1,
        "product_id": 1,
        "product_option_id": 2
    }
]
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명 : 로그인한 user의 주문목록 결과가 반환됩니다.

### 주문 등록 
[요청]
- URL: POST /api/products/order/items/

```bash
{
  "quantity": 3,
  "user_id": 1,
  "product_id": 1,
  "product_option_id": 2
} 
```
- Body 파라미터 설명
  - quantity : 상품 수량을 의미합니다.
  - user_id : 고객을 의미합니다.
  - product_id : 상품을 의미합니다.
  - product_option_id : 상품 옵션을 의미합니다.

[응답]
- Body
```bash
{
    "id": 12,
    "quantity": 3,
    "user_id": 1,
    "product_id": 1,
    "product_option_id": 2
}
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 201
  - 응답 Body 설명 : 주문 등록한 결과가 반환됩니다.

- Error

|에러코드|설명|
|------|-----|
|400| 파라미터 입력이 잘못된 경우|

### 주문 상세 조회
[요청]
- URL: GET /api/products/order/items/:pk/
  - Path 파라미터 설명 : pk는 items 식별 아이디를 입력합니다.

[응답]
- Body
```bash
{
    "id": 6,
    "quantity": 10,
    "product_id": 1,
    "user_id": 1,
    "product_option_id": 2,
    "product_name": "드레스",
    "product_option_size": "44",
    "product_option_color": "green"
}
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명 : 주문 상세 조회된 결과가 반환됩니다.

- Error

|에러코드|설명|
|------|-----|
|404| 주문 상품이 없는 경우|

### 주문 상품 수정
[요청]
- URL: PATCH /api/products/order/items/:pk/
  - Path 파라미터 설명 : pk는 items의 식별 아이디를 입력합니다.
- Body
```bash
{
  "quantity": 3
}
```
- Body 파라미터 설명
  - quantity : 상품수량을 의미합니다. 0 이상의 정수로만 입력해야 합니다.

[응답]
- Body
```bash
{
    "id": 7,
    "quantity": 3,
    "user_id": 1,
    "product_id": 1,
    "product_option_id": 2
}
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명  : 주 상품 수정된 결과가 반환됩니다.

- Error

|에러코드|설명|
|------|-----|
|400| 파라미터 입력이 잘못된 경우|

### 주문 삭제
[요청]
- URL: DELETE /api/products/order/items/:pk/
  - Path 파라미터 설명 : pk는 items의 식별 아이디를 입력합니다.

[응답]
- Body
```bash
{
  HTTP 204 No Content
}
```
- 응답에 대한 설명
  - 응답 Body 설명  : 내역이 삭제 됩니다.

### 관리자용 주문 조회
[요청]
- URL: GET /api/products/order/items/

[응답]
- Body
```bash
[
    {
        "id": 6,
        "quantity": 10,
        "user_id": 1,
        "product_id": 1,
        "product_option_id": 2
    },
    {
        "id": 7,
        "quantity": 2,
        "user_id": 1,
        "product_id": 1,
        "product_option_id": 2
    }
]
```
- 응답에 대한 설명
  - 성공 응답 시 상태코드 : 200
  - 응답 Body 설명 : 로그인한 user의 주문목록 결과가 반환됩니다.




  


