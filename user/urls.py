from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'user'
urlpatterns = [
    # path('login/',auth_views.LoginView.as_view(template_name = 'dist/index.html', next_page = 'movie:board1'),name='login'),
        ## django.contrib.auth.views를 import하여 내장 LoginView를 사용하는 url
        ## dist/index.html은 로그인기능과 회원가입기능이 같이있는 템플릿
    path('join/', views.UserCreateForm.as_view(),name='join'),
        ## 회원가입기능의 ClassView와 관련된 url
    path('join/', views.UserCreateForm.as_view(),name='join'),
    path('login/',auth_views.LoginView.as_view(template_name = 'dist/index.html', next_page = '/'),name='login'), 
    # path('login/', views.LoginClassView.as_view(), name='login'),

    path('logout/',auth_views.LogoutView.as_view(next_page = '/'),name='logout'),
        ## django.contrib.auth.views를 import하여 내장 LogoutView를 사용하는 url
        ## 로그아웃 후 이전페이지인 / 로 이동

    path('profile/', views.profile, name='profile'),
        ## 프로파일페이지와 관련된 뷰와 연결해주는 url
    path('delete_user_page/', views.delete_user_page, name='delete_user_page'),
        ## 회원탈퇴페이지와 관련된 뷰와 연결해주는 url
    path('delete_user/', views.delete_user, name='delete_user'), ## 원래사용하던 회원탈퇴url
        ## 회원탈퇴기능과 관련된 뷰와 연결해주는 url
    path('change_user_page/', views.userchangepage ,name='change_user_page'),
        ## 회원정보수정페이지와 관련된 뷰와 연결해주는 url
    path('<int:auth_user_id>/change_user/', views.userchangeview ,name='change_user'),
        ## 회원정보수정기능과 관련된 뷰와 연결해주는 url
    
    ######## 주석기준 위 url 사용중인 url / 아래 비사용 혹은 테스트중인 url
    
    # path('login/', views.LoginClassView.as_view(), name='login'),
    path('delete_user_test/', views.delete_user_test, name='delete_user_test'),
        ## 새로이 만들고자하는 회원탈퇴url
]
