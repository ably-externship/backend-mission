from .views import LionUserAPI, LionLoginUser, RegisterUser,LoginUser, loginTest, register, login,KakaoSignInView,kakaoTest, checkJwt,ApiRefreshRefreshTokenView,MyTokenObtainPairView

from django.urls import path

urlpatterns = [
    #회원가입 페이지
    path('register', register, name="register_page"),
    #로그인 페이지
    path('login', login, name="register_page"),

    path('login/test', loginTest, name="login_test"),
    path('login/kakao', kakaoTest, name="kakao_test"),

    path('lionregister', RegisterUser.as_view()),
    path('lionlogin', LoginUser.as_view()),

    path('lion', LionUserAPI.as_view()),  # create 회원가입
    path('lioncustomlogin', LionLoginUser.as_view()),

    path('kakao', KakaoSignInView.as_view()),
    path('check', checkJwt , name="check_jwt"),

    #refreshToken url #
    path('api/token/refresh/refresh_token/', ApiRefreshRefreshTokenView.as_view(),
         name='token_refresh_refresh_token'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

]