from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'user'
urlpatterns = [
    path('join/', views.UserCreateForm.as_view(),name='join'),
    path('login/',auth_views.LoginView.as_view(template_name = 'dist/index.html', next_page = '/'),name='login'), 
    # path('login/', views.LoginClassView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page = '/'),name='logout'),
    path('profile/', views.profile, name='profile'),
    path('delete_user_page/', views.delete_user_page, name='delete_user_page'),
    path('delete_user/', views.delete_user, name='delete_user'), ## 원래사용하던 회원탈퇴url
    # path('<int:auth_user_id>delete_user/', views.delete_user, name='delete_user'), ## 새로이 만들고자하는 회원탈퇴url
    path('change_user_page/', views.userchangepage ,name='change_user_page'),
    path('<int:auth_user_id>/change_user/', views.userchangeview ,name='change_user'),
]
