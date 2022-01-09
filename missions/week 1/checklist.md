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

## 프로젝트 
- 상품 상세 이미지 slide 적용을 위한 라이브러리 추가
   https://tailwind-elements.com/docs/standard/components/carousel/
- tailwind-cdd JIT모드
   bg-[#0d6efd]
- 메일 전송 관련 설정
  1. 메일 전송 설정 commons.py
      EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
      EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
      EMAIL_USE_TLS = True
      EMAIL_HOST = 'smtp.gmail.com'
      EMAIL_PORT = 587
      EMAIL_HOST_USER = 'v49011591@gmail.com'
      EMAIL_HOST_PASSWORD = 'cpvqpsmaybvewmlc'
      SERVER_EMAIL = 'v49011591@gmail.com'
      DEFAULT_FROM_MAIL = ''
  2. Gmail APP 계정 설정
    참고 : https://greensul.tistory.com/31
## TODO
  * 기능을 구현하는데에만 집중하여 코드 리팩토링 미흡
  * 상품 카테고리 DB 추가
  * 에러 처리에 대한 방법 확인 

