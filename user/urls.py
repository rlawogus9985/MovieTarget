from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'user'
urlpatterns = [
    path('join/', views.UserCreateForm.as_view(),name='join'),
    path('login/',auth_views.LoginView.as_view(template_name = 'user/login.html', next_page = '/'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page = '/'),name='logout'),

]
