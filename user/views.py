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
import json
import smtplib
from email.mime.text import MIMEText
from django.contrib.auth.hashers import check_password

## SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str #,django 4버젼 미만force_text
from .tokens import account_activation_token


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
@login_required(login_url=reverse_lazy('user:login'))
def  userchangeview(request):
# def  userchangeview(request, auth_user_id):
    """
    회원정보수정 기능과 관련된 함수 뷰이며
    현재 뷰 그리고 현재 뷰로 오도록한 url 그리고 url로 오도록한
    html template의 내의 urltemplates가 적힌  form에서 보내는 name을 활용
    """
    # auth_user.username 테이블 필드명 
    # username = request.POST.get('username', '') ## form에서 POST 형식으로 보낸 name명인 username을 get 해서 username이라는 변수명에 초기화 
    username = request.user.username
    auth_user_id=request.user.id
    password = request.POST.get('password', '') ## form에서 POST 형식으로 보낸 name명인 password을 get 해서 username이라는 변수명에 초기화 
    password2 = request.POST.get('password2', '') ## form에서 POST 형식으로 보낸 name명인 password2을 get 해서 username이라는 변수명에 초기화 
    try:
        if username == request.user.username and password == password2:
            user = auth_views.UserModel.objects.get(pk=auth_user_id)
            user.set_password(password)
            user.save()
            # return render(request, 'user/profile.html')
            return redirect(reverse_lazy('user:profile'))
        else:
            # return render(request, "user/user_change_page.html")
            return redirect(reverse_lazy('user:change_user_page'))
    except:
        # return render(request, 'user/profile.html')
        return redirect(reverse_lazy('user:profile'))

def password_check_ajax(request):
    id = request.user.id
    data = loads(request.body)
    wantnewpassword=data.get("changepassword1")
    user = auth_views.UserModel.objects.get(pk=id)
    
    if check_password(wantnewpassword,user.password):
        print('변경하고자하는 비밀번호가 현재 비밀번호와 일치합니다.')
        return JsonResponse({'result':'False'})
    else:
        print('변경하고자하는 비밀번호가 현재 비밀번호와 일치하지 않습니다.')
        return JsonResponse({'result':'True'})
    

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
# 자바스크립트 ajax와 연결되어 
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


################ 이메일 자바스크립트Ajax관련 함수뷰 
################ 이메일관련 함수뷰
# 자바스크립트 ajax와 연결되어 유저의 email 컬럼에 데이터가 존재하는지 여부를 확인하는 함수뷰
# @login_required(login_url=URL_LOGIN)
# @login_required(login_url=reverse_lazy('user:login'))
def ajax_confirm_email(request):
    user_id = request.user.id
    data = loads(request.body)
    
    targetuser = auth_views.UserModel.objects.get(id=user_id)
    print(targetuser.email)

    if len(targetuser.email) <= 0:
        print('해당유저의 이메일이 존재 하지 않음을 확인합니다.')
        return JsonResponse({'result': 'True'})
    else:
        print('해당유저의 이메일이 존재 함을 확인합니다.')
        return JsonResponse({'result': 'Fasle'})


# 자바스크립트 ajax와 연결되어 이메일을 작성해서 이메일을 보내는 함수뷰
# 구글링해서 얻은 코드를 일일영화 프로젝트에 맞게 커스텀한 함수뷰
# 필요는 없지만 토큰(token)과 먼지는 모르지만 uid를 생성 및 이동 시도하는 함수뷰
def ajax_token_email(request):
    data = loads(request.body)
    usereamil = data.get('userEmailId')
    useremaildomain = data.get('userEmailDomain')
    targetemail = usereamil+'@'+useremaildomain

    user_id = request.user.id
    user = auth_views.UserModel.objects.get(pk=user_id)
    
    current_site = get_current_site(request) 
    print('current_site : ', current_site)
    
    title = '일일영화설립 관련 이메일 입니다'
    message = render_to_string('user/activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'targetemail':targetemail,
        })
    print('message', message)
    email = EmailMessage(title,message,to=[targetemail])
    
    # if targetemail.find('.') is False:
    #     print('이메일의 형식 잘못되었습니다.')
    #     return JsonResponse({'result': 'False'})
    if auth_views.UserModel.objects.filter(email=targetemail):
        print('이미등록된 이메일입니다.')
        return JsonResponse({'result': 'False'})
    elif auth_views.UserModel.objects.filter(pk=user_id).exists():
        email.send()
        print('이메일 보냈습니다.')
        return JsonResponse({'result': 'True'})
    else:
        print('대상이 되는 이메일이 없습니다.')
        return JsonResponse({'result': 'False'})


# 이메일에서 클릭하라는 부분은 클릭시 데이터를 받아온 url이 데이터를 전해주고 그 데이터를 가지고 유저의 email을 업데이트(등록)해주는 함수뷰
def activate(request, uidb64, token, targetemail):
    print('targetemail',targetemail)
    user_id = request.user.id
    user = auth_views.UserModel.objects.get(pk=user_id)
    # if len(user.email) <= 0:
    if len(user.email) <= 0:
        auth_views.UserModel.objects.filter(pk=user_id).update(email=targetemail)
        print("영화사 이메일이 등록되었습니다.")
        return redirect('movie:board1')
    else:
        print("영화사 이메일이 이미 존재하는 유저입니다.")
        return redirect('movie:board1')

def ajax_to_find_confirm_email(request):
    data = loads(request.body)
    usereamil = data.get('emailName')
    useremaildomain = data.get('emailDomain')
    targetemail = usereamil+'@'+useremaildomain
    print('targetemail',targetemail)

    user = auth_views.UserModel.objects.get(email=targetemail)
    username=user.username
    if auth_views.UserModel.objects.filter(email=targetemail).exists():
        print('아이디 찾기를 위한 이메일이 데이터베이스에 존재합니다.')
        print('username은' ,username)

        current_site = get_current_site(request) 

        title = '일일영화 아이디 찾기와 관련된 이메일입니다'
        message = render_to_string('user/find_id_email.html', {
            'username': username,
            'domain': current_site.domain,
            'targetemail':targetemail,
            })
        print('message', message)
        email = EmailMessage(title,message,to=[targetemail])
        email.send()
        print('아이디 찾기 이메일보내기 완료했습니다.')

        return JsonResponse({'result': 'True'})
    else:
        print('아이디 찾기를 위한 이메일이 데이터베이스에 존재하지 않습니다.')
        return JsonResponse({'result': 'False'})

def findpasswordreset(request):
    data = loads(request.body)
    userName = data.get('userName')
    emailName = data.get('emailName')
    emailDomain = data.get('emailDomain')
    targetemail = emailName+'@'+emailDomain
    print('userName :', userName)
    print('targetemail :',targetemail)

    if auth_views.UserModel.objects.filter(username=userName,email=targetemail).exists():

        print('비밀번호를 찾기를 위한 아이디와 이메일이 일치하는 데이터가 데이터베이스에 존재합니다.')

        # 아래 한줄 새로 추가한 코드
        user=auth_views.UserModel.objects.filter(username=userName,email=targetemail)
        
        current_site = get_current_site(request) 
        title = '일일영화 비밀번호 찾기와 관련된 이메일입니다'
        message = render_to_string('user/find_pw_emai.html', {
            'username': userName,
            'domain': current_site.domain,
            'targetemail':targetemail,

            #아래 두줄 새로 추가한코드
            # 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            # 'token': account_activation_token.make_token(user),
            })
        print('message', message)
        email = EmailMessage(title,message,to=[targetemail])
        email.send()
        print('비밀번호를 찾기를 위한 이메일보내기 완료했습니다.')

        return JsonResponse({'result': 'True'})
        
    else:
        print('비밀번호를 찾기를 위한 아이디와 이메일이 일치하는 데이터가 데이터베이스에 존재하지않습니다')
        return JsonResponse({'result': 'False'})

# @login_required(login_url='login')
def emailresetpassword(request, username, targetemail):
    print(username,targetemail)
    return render(request,'user/to_rest_input_password.html')


def fromeamilpasswordreset(requset):
    data=loads(requset.body)
    resetid=data.get('resetID')
    resetpassword1=data.get('resetPassword1')
    resetpassword2=data.get('resetPassword2')
    print('restid : ',resetid)
    print('resetpassword1 : ', resetpassword1)
    print(type(resetpassword1))

    # 'uid': urlsafe_base64_encode(force_bytes(user.pk))
    # 'token': account_activation_token.make_token(user)


    import bcrypt
    if auth_views.UserModel.objects.filter(username=resetid).exists():

        # resetpassword1 = bcrypt.hashpw(resetpassword1.encode('utf-8'), bcrypt.gensalt())
        # print('resetpassword1에 관한정보 : ',resetpassword1, type(resetpassword1))
        
        user=auth_views.UserModel.objects.get(username=resetid)
        user.set_password(resetpassword1)
        user.save()

        # user.set_password(self.cleaned_data["password1"])

        # auth_views.UserModel.objects.filter(username=resetid).update(password=resetpassword1)

        # print('user type은?', type(user))
        # u=auth_views.UserModel.objects.filter(username=resetid)#.set_password(resetpassword1)
        # u.update
        # u.set_password(resetpassword1)
        # u.save()
        print(f'{resetid}의 비밀번호가 변경되었습니다.')
        # return render(requset, 'dist/index.html')
        return JsonResponse({'result':'True'})
    else:
        return JsonResponse({'result': 'Fasle'})


def toresetpasswordfindemail(requset):
    data=loads(requset.body)
    resetid=data.get('resetID')
    print(resetid)
    if auth_views.UserModel.objects.filter(username=resetid):
        print('타켓유저가 존재합니다.')
        return JsonResponse({'result': 'True'})
    else:
        print('타켓유저가 존재하지않습니다.')
        return JsonResponse({'result':' Flase'})

def toresetpasswordcheckpassword(request):
    data = loads(request.body)
    resetID=data.get("resetID")
    resetPassword1=data.get("resetPassword1")
    user=auth_views.UserModel.objects.get(username=resetID)
    if check_password(resetPassword1, user.password):
        print('변경하고자 하는 비밀번호와 현재 비밀번호가 일치합니다 다시 입력해주세요.')
        return JsonResponse({'result':'False'})
    else:
        return JsonResponse({'result':'True'})


############## 지금은 사용하지 않는 이메일등록 함수뷰 
# # @login_required(login_url=URL_LOGIN)
# # @login_required(login_url=reverse_lazy('user:login'))
# def constitution_email(request):
#     user_id = request.user.id
#     # userauth = auth_views.UserModel()
#     email_name = request.POST.get('emailname', '')
#     emaildomain = request.POST.get('emaildomain', '')
#     print(email_name+'@'+emaildomain)
#     email=email_name+'@'+emaildomain
#     user = auth_views.UserModel.objects.get(pk=user_id)
#     if len(user.email) <= 0:
#         auth_views.UserModel.objects.filter(pk=user_id).update(email=email)
#         print("영화사 이메일이 등록되었습니다.")
#         return redirect('movie:board1')
#     else:
#         print("이미 비활성화 되어있는 유저입니다.")
#         return redirect('movie:board1')
##################################################
  