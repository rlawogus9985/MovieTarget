from django.http import Http404, JsonResponse
from django.shortcuts import  redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CheckPasswordForm, CustommUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import AbstractUser
from django.views import View

from user.decorators import * # 함수형 뷰 데코
# from django.utils.decorators import method_decorator # 클래스기반뷰에사용 데코
# from django.contrib.auth.decorators import login_required # django 내장 데코


def login(request):
    return render(request, 'dist/index.html')

@login_required(login_url=reverse_lazy('user:login'))
def profile(request):
    return render(request, 'user/profile.html')

@login_required(login_url=reverse_lazy('user:login'))
def delete_user_page(request):
    return render(request, 'user/user_delete.html')

class UserCreateForm(generic.CreateView):
    form_class = auth_forms.UserCreationForm
    template_name = 'dist/index.html' # get 방식일 경우 회원가입유도
    success_url = reverse_lazy('user:login') # post 방식일 경우 리다이렉트로 로그인으로 가는상황

@login_required(login_url=reverse_lazy('user:login'))
def userchangepage(request):
    return render(request, "user/user_change_page.html")


@login_required(login_url=reverse_lazy('user:login'))
def  userchangeview(request, auth_user_id):
    # auth_user.username 테이블 필드명 
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    password2 = request.POST.get('password2', '')
    try:
        if username == request.user.username and password == password2:
            user = auth_views.UserModel.objects.get(pk=auth_user_id)
            user.set_password(password)
            user.save()
            return render(request, 'user/profile.html')
        else:
            return render(request, "user/user_change_page.html")
            
    except:
        return render(request, 'user/profile.html')
    
## 테스트중인 새로운 클래스뷰
# @login_required(login_url=reverse_lazy('user:login'))
# class LoginClassView(View):
#     model = auth_views.UserModel
#     fields = ['username', 'password']
#     template_name = 'dist/index.html'
    

    # def post(self, request):
    #     data = json.loads(request.body)
    #     try:
    #         username    = data['username']
    #         password = data['password']

    #         if not auth_views.UserModel.objects.filter(username=username).exists():
    #             return JsonResponse({'error': 'INVALID_USER'}, status=401)
    #         if auth_views.UserModel.objects.get(username=username).password == password:
    #             return JsonResponse({'message':'SUCCESS'}, status=200)
    #         return JsonResponse({'error': 'INVALID_USER'}, status=401)

    #     except KeyError:
    #         return JsonResponse({'error': 'KEY_ERROR'}, status=400)

# 원래 사용하던 유저탈퇴 함수뷰
@require_POST
@login_required(login_url=reverse_lazy('user:login'))
def delete_user(request):
    request.user.delete()
    # request.user.is_active()

    return redirect('user:join')

## delete() 하지않고 is_active를 0으로 변환시킬 새로운 회원탈퇴함수뷰.
# @require_POST
# @login_required(login_url=reverse_lazy('user:login'))
# def delete_user(request):
#     pk = request.user.id
#     user =  auth_views.UserModel.objects.get(pk=pk)
#     now_is_active = user.is_active
#     auth_views.UserModel.objects.update(is_active= now_is_active)
#     return redirect('user:join')

