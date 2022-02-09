FROM nginx:latest
# 이미지 안의 default.conf에 도커가 제공하는 nginx의 기본 설정 삭제
RUN rm /etc/nginx/conf.d/default.conf
# 로컬에서 새로 만든 nginx 설정 정보를 nginx 이미지에 복사
COPY nginx.conf /etc/nginx/conf.d