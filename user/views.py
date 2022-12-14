from django.http import Http404, JsonResponse
from django.shortcuts import  redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST#, require_http_methods
from .forms import CheckPasswordForm, CustommUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import AbstractUser
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
from movie.models import SelectedBase
from django.contrib import messages
from user.decorators import * # 함수형 뷰 데코
from django.utils.decorators import method_decorator # 클래스기반뷰에사용 데코
from json import loads
from django.contrib.auth.hashers import check_password

## 비밀번호 재설정 토큰관련 모듈
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.http import HttpResponse
# from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# 비밀번호 재설정 토큰관련 함수뷰
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = get_user_model().objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = '[일일영화] 비밀번호 재설정'
					email_template_name = "account/password_reset_email.txt"
					c = {
						"email": user.email,
						# local: '127.0.0.1:8000', prod: 'givwang.herokuapp.com'
						'domain': settings.HOSTNAME,
						'site_name': 'givwang',
						# MTE4
						"uid": urlsafe_base64_encode(force_bytes(user.pk)),
						"user": user,
						# Return a token that can be used once to do a password reset for the given user.
						'token': default_token_generator.make_token(user),
						# local: http, prod: https
						'protocol': settings.PROTOCOL,
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'dailydailymovie@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(
		request=request,
		template_name='account/password_reset.html',
		context={'password_reset_form': password_reset_form})



class UserCreateForm(generic.CreateView):
    """ django.views.generic.CreateView 내장뷰를 상속받는 회원가입관련 클래스 뷰"""
    form_class = auth_forms.UserCreationForm # django.contib.auth.forms.UserCreationForm 내장폼을 form_class 변수명에 지정
    template_name = 'dist/index.html' # get 방식일 경우 회원가입유도
    success_url = reverse_lazy('user:login') # post 방식일 경우 리다이렉트로 로그인으로 가는상황


class UserLoginView(LoginView):
    template_name = 'dist/index.html'  #가입하기템플릿으로 가라.

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)


# 유저가 선택한 데이터가 있는 게시판을 만들기 위한 view
class UserSelectedDataView(generic.ListView):
    # model = SelectedBase
    paginate_by = 12
    template_name = 'user/user_selected_data.html'
    context_object_name = "selecteddata_list"

    def get_queryset(self):
        
        result = SelectedBase.objects.order_by('-id').filter(writer_id=self.request.user)
        return result
    
URL_LOGIN = '/user/login/'

# @login_required(login_url=URL_LOGIN)
@login_required(login_url=reverse_lazy('user:login'))
def profile(request):
    """
    프로파일과 관련된 html으로 render하는 함수뷰,
    login_required 데코레이션을 사용하여 로그인이 되어있지 않을경우,
    reverse_lazy 로 user:login로 로그인유도."""
    return render(request, 'user/profile.html')


# @login_required(login_url=reverse_lazy('user:login'))
# @login_required(login_url=URL_LOGIN)
def delete_user_page(request):
    """
    회원탈퇴 관련된 html으로 render하는 함수뷰,
    login_required 데코레이션을 사용하여 로그인이 되어있지 않을경우,
    reverse_lazy 로 user:login로 로그인유도."""
    return render(request, 'user/user_delete.html')


# @login_required(login_url=reverse_lazy('user:login'))
# @login_required(login_url=URL_LOGIN)
def userchangepage(request):
    """
    회원정보수정과 관련된 html으로 render하는 함수뷰,
    login_required 데코레이션을 사용하여 로그인이 되어있지 않을경우,
    reverse_lazy 로 user:login로 로그인유도."""
    return render(request, "user/user_change_page.html")


# @login_required(login_url=URL_LOGIN)
# @login_required(login_url=reverse_lazy('user:login'))
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



# delete() 하지않고 is_active를 0으로 update()할 새로운 회원탈퇴함수뷰.
# @login_required(login_url=URL_LOGIN)
# @require_POST
# @login_required(login_url=reverse_lazy('user:login'))
def delete_user(request):
    
    userid = request.user.id 
    # userauth = auth_views.UserModel()
    
    # user =  auth_views.UserModel.objects.get(pk=userid)
    # user =  auth_views.UserModel.objects.get_object_or_404(pk=userid)
    if auth_views.UserModel.objects.get(pk=userid):
        auth_views.UserModel.objects.filter(pk=userid).update(is_active=False)
        # userauth.save(pk=)
        print("해당유저가 비활성화 되었습니다.")
        return redirect('user:join')
    else:
        print("이미 비활성화 되어있는 유저입니다.")
        return redirect('user:join')


def login(request):
    return render(request, 'dist/index.html')

############## Ajax 함수뷰

# 원본 ajax singup view 함수 제대로 되는것!!!
def ajax_user_signup(request):
    data = loads(request.body)
    ajax_username = data.get('signupname')
    
    targetuser = auth_views.UserModel.objects.filter(username=ajax_username)

    # print(targetuser)

    if targetuser.count() > 0:
        return JsonResponse({'result': 'False'})
    else:
        return JsonResponse({'result': 'True'})

    
# 원본 ajax login view 함수

def ajax_user_login(request):
    data = loads(request.body)
    ajax_username = data.get('loginname')
    ajax_password = data.get('loginpassword')

    targetuser = auth_views.UserModel.objects.filter(username=ajax_username)
    # auth_views.UserModel.objects.filter(username=ajax_username)
    # targetpassword = targetuser.set_password
    # targetpassword = targetuser.password
    # if targetuser.couont() > 0 and targetpassword == ajax_password:
    if targetuser.count() > 0:
        return JsonResponse({'result': 'True'})
    else:
        return JsonResponse({'result': 'False'})

# ## 테스트중인 ajax login view 로그인을 form클래스 및 내장form템플릿을 사용했을경우 쓸수 있나봄...
# def ajax_user_login(request, self):
#     data = loads(request.body)
#     ajax_username = data.get('loginname')
#     ajax_password = data.get('loginpassword')
#     if ajax_username and ajax_password:
#         user = auth_views.UserModel.objects.get(username=ajax_username)
#         if not check_password(ajax_password, user.username):
#             self.add_error('password', '비밀번호가 틀렸습니다.')

#### 이메일 Ajax뷰
# @login_required(login_url=URL_LOGIN)
# @login_required(login_url=reverse_lazy('user:login'))
def ajax_confirm_email(request):
    user_id = request.user.id
    data = loads(request.body)
    
    targetuser = auth_views.UserModel.objects.get(id=user_id)
    print(targetuser.email)
    # targetuser = auth_views.UserModel.objects.filter(email=email)
    if len(targetuser.email) <= 0:
        print('해당유저의 이메일이 존재 하지 않음을 확인합니다.')
        return JsonResponse({'result': 'True'})
    else:
        print('해당유저의 이메일이 존재 함을 확인합니다.')
        return JsonResponse({'result': 'Fasle'})


############## 이메일 함수뷰
@login_required(login_url=URL_LOGIN)
# @login_required(login_url=reverse_lazy('user:login'))
def constitution_email(request):
    user_id = request.user.id
    # userauth = auth_views.UserModel()
    email_name = request.POST.get('emailname', '')
    emaildomain = request.POST.get('emaildomain', '')
    print(email_name+'@'+emaildomain)
    email=email_name+'@'+emaildomain
    user = auth_views.UserModel.objects.get(pk=user_id)
    if len(user.email) <= 0:
        auth_views.UserModel.objects.filter(pk=user_id).update(email=email)
        print("영화사 이메일이 등록되었습니다.")
        return redirect('movie:board1')
    else:
        print("이미 비활성화 되어있는 유저입니다.")
        return redirect('movie:board1')
##################################################

#애 쓰고 주석처리안하면 무한방복문 걸림
# -*- coding:utf-8 -*-
 
# import smtplib
# from email.mime.text import MIMEText
 
# smtp = smtplib.SMTP('smtp.live.com', 587)
# smtp.ehlo()      # say Hello
# smtp.starttls()  # TLS 사용시 필요
# smtp.login('lee@live.com', 'password')
 
# msg = MIMEText('본문 테스트 메시지')
# msg['Subject'] = '테스트'
# msg['To'] = 'kim@naver.com'
# smtp.sendmail('lee@live.com', 'kim@naver.com', msg.as_string())
 
# smtp.quit()


######### 토큰함수뷰
def ajax_token_email(request):

    user_id = request.user.id
    targetuser = auth_views.UserModel.objects.get(id=user_id)
    print(targetuser.email)
    # targetuser = auth_views.UserModel.objects.filter(email=email)
    if len(targetuser.email) <= 0:
        print('해당유저의 이메일이 존재 하지 않음을 확인합니다.')
        return JsonResponse({'result': 'True'})
    else:
        print('해당유저의 이메일이 존재 함을 확인합니다.')
        return JsonResponse({'result': 'Fasle'})

########## 위 사용하는 뷰 아래 비사용혹은 테스트중인 뷰


#########
# @require_POST
# @login_required(login_url=reverse_lazy('user:login'))
# def delete_user(request):

#     userid = request.user.id 
#     user =  auth_views.UserModel.objects.get(pk=userid) 
#     if user.is_active:
#         request.user.objects.update(is_active=0)
#         user.save()
#         print("해당유저가 비활성화 되었습니다.")
#         return redirect('user:join')
#     else:
#         print("이미 비활성화 되어있는 유저입니다.")
#         return redirect('user:join')

def login(request):
    return render(request, 'dist/index.html')
# 로그인할때 사용하는 클래스 함수.
# 로그인 이후 넘어가는 화면은 settings.py 의 Login_redirect_url

## 테스트중인 새로운 클래스뷰
@login_required(login_url=reverse_lazy('user:login'))
class LoginClassView(View):
    model = auth_views.UserModel
    fields = ['username', 'password']
    template_name = 'dist/index.html'
    

    def post(self, request):
        data = json.loads(request.body)
        try:
            username    = data['username']
            password = data['password']

            if not auth_views.UserModel.objects.filter(username=username).exists():
                return JsonResponse({'error': 'INVALID_USER'}, status=401)
            if auth_views.UserModel.objects.get(username=username).password == password:
                return JsonResponse({'message':'SUCCESS'}, status=200)
            return JsonResponse({'error': 'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'error': 'KEY_ERROR'}, status=400)

# 원래 사용하던 유저탈퇴 함수뷰
# @require_POST
# @login_required(login_url=reverse_lazy('user:login'))
# def delete_user(request):
#     request.user.delete()
#     # request.user.is_active()

#     return redirect('user:join')

