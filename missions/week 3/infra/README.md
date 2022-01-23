# 젠킨스 운영 매뉴얼

 * ec2의 메모리 부족으로 기존에 띄워놨던 Django 어플리케이션을 삭제하고 jenkins를 빌드 해놓은 상태입니다.
 * docker jenkins build 명령어
    - sudo docker run  -v -d /home/ubuntu/jenkins:/var/jenkins_home -p 80:8080 -p 50000:50000 -e TZ=Asia/Seoul jenkins/jenkins
 * 접속 URL : http://www.kj-dev.com
 * 아이디 : root
 * 비밀번호 : ably123!@#

# webhook 동작 방법
 * github setting에서 webhook 설정에 payload url - http://www.kj-dev.com/github-webhook/ 등록 및 content-type application/json으로 변경
 * jenkins에서 새로운 Item 생성
   - Item 구성 화면에 접속
   - 소스 코드 관리 Git 선택 후 backend-mission Repository 주소 입력 후 사용자 계정 입력
   - 빌드 유발 항목에서  GitHub hook trigger for GITScm polling 체크
   - Build -> Add build step에서 Execute Shell 선택 후 Command에 touch  $(date +%Y_%m_%d%_H_%M_%S).log 입력 후 저장

