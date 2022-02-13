# 과제 체크 리스트

## 자유로운 작품을 만들어주세요.

- 쇼핑몰과 관련된 주제라면 뭐든 괜찮습니다.
- 참고로 에이블리 개발자 분들이 주로 사용하시는 기술스택은 장고 DRF, MySQL, 엘라스틱서치 입니다.
- 이번 작품에 에이블리 개발자 분들에게 어필할 수 있는 부분을 만드는게 취업에 유리합니다.

## 수행인증영상URL(유튜브)

- https://youtu.be/Szk3TDdJC1Y
- 위 링크를 지우고 여러분의 영상 링크를 남겨주세요.
- 영상을 일부공개로 설정해주세요, 링크가 있는 분들만 볼 수 있습니다.


* 개발,운영 환경 분리

* Custom Command
    * init_data 를 통해 기본 데이터 셋팅
        * python manage.py init_data
    * 가짜 데이터를 활용하여 원하는 수만큼의 제품 생성
        * python manage.py seed_products —number 100 (100개의 제품 생성)

* DRF , CBV 활용한 API 개발
    * APIView, Generic, ModelViewSet 활용

* React 와 DRF 연동
    * 로그인/로그아웃
    * 기본적인 CRUD

* Dockerizing
    * nginx
    * django
    * db

* Swagger 연동
    * OAS3 (drf-yasg는 3버전을 지원하지 않아 drf-spectacular사용)

* S3 연동
    * Image upload