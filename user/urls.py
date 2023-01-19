from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView
app_name = 'user'
urlpatterns = [
    # path('login/',auth_views.LoginView.as_view(template_name = 'dist/index.html', next_page = 'movie:board1'),name='login'),
        # django.contrib.auth.views를 import하여 내장 LoginView를 사용하는 url
        # dist/index.html은 로그인기능과 회원가입기능이 같이있는 템플릿
    path('join/', views.UserCreateForm.as_view(),name='join'),
        # 회원가입기능의 ClassView와 관련된 url
    # path('join/', views.UserCreateForm.as_view(),name='join'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('login/',auth_views.LoginView.as_view(template_name = 'dist/index.html', next_page = '/'),name='login'), 
    # path('login/', views.LoginClassView.as_view(), name='login'),

    path('logout/',auth_views.LogoutView.as_view(next_page = '/'),name='logout'),
        # django.contrib.auth.views를 import하여 내장 LogoutView를 사용하는 url
        # 로그아웃 후 이전페이지인 / 로 이동

    path('profile/', views.profile, name='profile'),
        # 프로파일페이지와 관련된 뷰와 연결해주는 url
    path('profile/selected/', views.UserSelectedDataView.as_view(), name='selected_data'),
    
    path('delete_user_page/', views.delete_user_page, name='delete_user_page'),
        # 회원탈퇴페이지와 관련된 뷰와 연결해주는 url
    path('delete_user/', views.delete_user, name='delete_user'),
        # 새로이 만들고자하는 회원탈퇴url

    path('password_check_ajax/', views.password_check_ajax, name='password_check_ajax'),
    # 비밀번호 변경시 현재의 비밀번호와 동일한 비밀번호로 변경하지 못하도록 하는 비밀번호 체크 ajax 함수

    path('change_user_page/', views.userchangepage ,name='change_user_page'),
        # 회원정보수정페이지와 관련된 뷰와 연결해주는 url
    path('change_user/', views.userchangeview ,name='change_user'),
    # path('<int:auth_user_id>/change_user/', views.userchangeview ,name='change_user'),
        # 회원정보수정기능과 관련된 뷰와 연결해주는 url
    
    path('ajax_user_login/', views.ajax_user_login, name='ajax_user_login'),
        # 로그인 관련 ajax view함수  

    path('ajax_user_signup/', views.ajax_user_signup, name='ajax_user_signup'),
        # 회원가입 관련 ajax view함수

    ####### 주석기준 위 url 사용중인 url / 아래 비사용 혹은 테스트중인 url
    
    # 
    # path('constitution_email/', views.constitution_email, name='constitution_email'),
        # 영화사 이메일 등록관련 view함수

    path('ajax_confirm_email/', views.ajax_confirm_email, name='ajax_confirm_email'),
        # 영화사 이메일 확인관련 ajax view함수

    path('delete_user/', views.delete_user, name='delete_user'), ## 원래사용하던 회원탈퇴url
        # 회원탈퇴기능과 관련된 뷰와 연결해주는 url
    # path('login/', views.LoginClassView.as_view(), name='login'),

    #######
    # 비밀번호 재설정 토큰관련 url
    path('password_reset/', views.password_reset_request, name="password_reset"),

    # # 원본 이메일 보내기 
    path('ajax_token_email/', views.ajax_token_email, name="ajax_token_email"),

    # # 테스트용 이메일 보내기
    # path('ajax_token_email/', views.AjaxTokenEmail, name='ajax_token_email'),
    #     # 영화사 이메일 확인관련 ajax view함수

    # 이메일에서 클릭하라는 부분 클릭시 데이터를 받아내는 url 그 받은데이터를 activate view에 전달을 한다
    path('activate/<str:uidb64>/<str:token>/<str:targetemail>', views.activate, name="activate"),

    path('ajax_to_find_confirm_email/', views.ajax_to_find_confirm_email, name="ajax_to_find_confirm_email"),


    path('findpasswordreset/', views.findpasswordreset, name="findpasswordreset"),
    path('emailresetpassword/<str:username>/<str:targetemail>', views.emailresetpassword, name="emailresetpassword"),

    
    path('fromeamilpasswordreset/', views.fromeamilpasswordreset, name='fromeamilpasswordreset'),


    path('toresetpasswordfindemail/', views.toresetpasswordfindemail, name='toresetpasswordfindemail'),

    path('toresetpasswordcheckpassword/', views.toresetpasswordcheckpassword, name='toresetpasswordcheckpassword'),

    
]
