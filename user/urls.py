from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'user'
urlpatterns = [
    path('join/', views.UserCreateForm.as_view(),name='join'),
    path('login/',auth_views.LoginView.as_view(template_name = 'dist/index.html', next_page = 'movie:board'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page = '/'),name='logout'),
    path('profile/', views.profile, name='profile'),
    path('delete_user_page/', views.delete_user_page, name='delete_user_page'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('change_user_apge/', views.userchangepage ,name='change_user_page'),
    path('change_user/', views.UserChangeForm.as_view() ,name='change_user'),
    
]
