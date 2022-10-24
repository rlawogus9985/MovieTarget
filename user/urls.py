from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='user/login.html',
        next_page='/'
    ), name='login'),
]
