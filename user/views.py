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

class UserCreateForm(generic.CreateView):
    """ django.views.generic.CreateView 내장뷰를 상속받는 회원가입관련 클래스 뷰"""
    form_class = auth_forms.UserCreationForm # django.contib.auth.forms.UserCreationForm 내장폼을 form_class 변수명에 지정
    template_name = 'dist/index.html' # get 방식일 경우 회원가입유도
    success_url = reverse_lazy('user:login') # post 방식일 경우 리다이렉트로 로그인으로 가는상황

@login_required(login_url=reverse_lazy('user:login'))
def profile(request):
    """
    프로파일과 관련된 html으로 render하는 함수뷰,
    login_required 데코레이션을 사용하여 로그인이 되어있지 않을경우,
    reverse_lazy 로 user:login로 로그인유도."""
    return render(request, 'user/profile.html')

@login_required(login_url=reverse_lazy('user:login'))
def delete_user_page(request):
    """
    회원탈퇴 관련된 html으로 render하는 함수뷰,
    login_required 데코레이션을 사용하여 로그인이 되어있지 않을경우,
    reverse_lazy 로 user:login로 로그인유도."""
    return render(request, 'user/user_delete.html')

@login_required(login_url=reverse_lazy('user:login'))
def userchangepage(request):
    """
    회원정보수정과 관련된 html으로 render하는 함수뷰,
    login_required 데코레이션을 사용하여 로그인이 되어있지 않을경우,
    reverse_lazy 로 user:login로 로그인유도."""
    return render(request, "user/user_change_page.html")

@login_required(login_url=reverse_lazy('user:login'))
def  userchangeview(request, auth_user_id):
    """
    회원정보수정 기능과 관련된 함수 뷰이며
    현재 뷰 그리고 현재 뷰로 오도록한 url 그리고 url로 오도록한
    html template의 내의 urltemplates가 적힌  form에서 보내는 name을 활용
    """
    # auth_user.username 테이블 필드명 
    username = request.POST.get('username', '') ## form에서 POST 형식으로 보낸 name명인 username을 get 해서 username이라는 변수명에 초기화 
    password = request.POST.get('password', '') ## form에서 POST 형식으로 보낸 name명인 password을 get 해서 username이라는 변수명에 초기화 
    password2 = request.POST.get('password2', '') ## form에서 POST 형식으로 보낸 name명인 password2을 get 해서 username이라는 변수명에 초기화 
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

# 원래 사용하던 유저탈퇴 함수뷰
@require_POST
@login_required(login_url=reverse_lazy('user:login'))
def delete_user(request):
    request.user.delete()
    # request.user.is_active()

    return redirect('user:join')

########## 위 사용하는 뷰 아래 비사용혹은 테스트중인 뷰

# delete() 하지않고 is_active를 0으로 update()할 새로운 회원탈퇴함수뷰.
@require_POST
@login_required(login_url=reverse_lazy('user:login'))
def delete_user_test(request):

    userid = request.user.id 
    user =  auth_views.UserModel.objects.get(pk=userid) 
    if user.is_active == 1:
        request.user.update(is_active=0)
        user.save()
        print("해당유저가 비활성화 되었습니다.")
        return redirect('user:join')
    else:
        print("이미 비활성화 되어있는 유저입니다.")
        return redirect('user:join')

def login(request):
    return render(request, 'dist/index.html')
    
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




