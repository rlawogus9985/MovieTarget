"""box_office URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views # 이메일로 비밀번호 재설정의 위한 import
# from restFrameWork import views
# from  restFrameWork import views 

# # 5-1. RestTemplate and FASTAPI
# from django.contrib.auth.models import User # Django를 Client를 만들기위한, api-auth를 위한 Django 내장 User 객체 import하기 
# from rest_framework import routers, serializers, viewsets   # 먼지는 모르겠지만 Django REST framework 사이트를 따라가면서 import하기

# # 5-2. Serializers define the API representation # import한 Serializers 모듈로 API대표자대리인표현을 정의하기
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         Model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # 5-3. ViewSets 모듈로 view의 behavior을 정의하기
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # 5-4. Routers가 자동으로 쉽게 환경설정배열(configuration) 결정할수 있도록 제공한다
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)   #처음보는것 f''String같은거  r'' -> RawString ESCAPE문법을 ESCAPE하지못하도록 제어
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='common/home.html'), name='home'),
    path("movie/", include("movie.urls")),
    path("user/", include("user.urls")),
    # path('password/', include('django.contrib.auth.urls')),

    # 비밀번호 재설정 토큰관련 url
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),

    # api-auth RestTemplate를 위한 root url 설정
    # 6. 우리의 API객체를 자동으로 URL을 전달하고, 우리는 추가적으로 브라우저 API를 위한 로그인 URL들을 include
    # path('api-auth/', include('restFrameWork.urls', namespace='restFrameWork')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

