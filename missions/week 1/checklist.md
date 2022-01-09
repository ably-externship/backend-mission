# 과제 체크 리스트

## 체크리스트

- [x] 모바일 UI
- [x] 쇼핑몰 상품 리스트
- [x] 쇼핑몰 상품 리스트, 검색
- [x] 쇼핑몰 상품 리스트, 페이징
- [x] 쇼핑몰 상품 상세페이지
- [x] 회원가입
- [x] 로그인
- [x] 상품질문기능 구현
- [ ] 추가과제
- [x] 반응형 UI
- [x] 부트스트랩 5 적용
- [ ] 테일윈드 3.0, JIT 모드 적용(?)
- [x] 장고 부트스트랩 5(django-bootstrap5) 라이브러리를 이용해서 폼 출력
- [x] 아이디찾기
- [x] 이메일을 통한 비빌번호 찾기(혹은 패스워드 리셋)

## 수행인증영상URL(유튜브)
-

## 라이브러리 활용 및 Django 설정
- 상품 상세 이미지 slide 적용을 위한 라이브러리 추가
   https://tailwind-elements.com/docs/standard/components/carousel/
- tailwind-cdd JIT모드
   bg-[#0d6efd]
- 메일 전송 관련 설정
  1. 메일 전송 설정 commons.py
      EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'\n
      EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'\n
      EMAIL_USE_TLS = True\n
      EMAIL_HOST = 'smtp.gmail.com'\n
      EMAIL_PORT = 587\n
      EMAIL_HOST_USER = 'v49011591@gmail.com'\n
      EMAIL_HOST_PASSWORD = 'cpvqpsmaybvewmlc'\n
      SERVER_EMAIL = 'v49011591@gmail.com'\n
      DEFAULT_FROM_MAIL = ''\n
  2. Gmail APP 계정 설정
    참고 : https://greensul.tistory.com/31
    
## 질문
 * 현재 상품 옵션 테이블에 size, color 컬럼을 추가하였는데 만약 옵션에 대한 내용이 추가되면 컬럼을 추가 하는 방식이 아닌 code값과 value 형식의 테이블로 변경 하는 것이 더 합리적이라고 생각합니다. 이런 방식으로 테이블 구조를 변경하게 되면 옵션에 따른 재고 관리가 어려울거 같아 보이는데 관련해서 참고해볼만한 내용이 있는지 질문 드립니다. 
## TODO
  * 기능을 구현하는데에만 집중하여 코드 리팩토링 미흡
  * 상품 카테고리 DB 추가
  * 에러 처리에 대한 방법 확인
  * docker 이미지는 생성하였는데 build가 안되는 현상 확인(config관련 문제인것 같음)

