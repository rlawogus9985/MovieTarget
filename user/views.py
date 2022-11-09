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
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
from movie.models import SelectedBase

from user.decorators import * # 함수형 뷰 데코
# from django.utils.decorators import method_decorator # 클래스기반뷰에사용 데코
# from django.contrib.auth.decorators import login_required # django 내장 데코

from json import loads

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
# @require_POST
# @login_required(login_url=reverse_lazy('user:login'))
# def delete_user(request):
#     request.user.delete()
#     # request.user.is_active()

#     return redirect('user:join')

# delete() 하지않고 is_active를 0으로 update()할 새로운 회원탈퇴함수뷰.
@require_POST
@login_required(login_url=reverse_lazy('user:login'))
def delete_user(request):

    userid = request.user.id 
    userauth = auth_views.UserModel()
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

########### Ajax 함수뷰

def ajax_user_signup(request):
    data = loads(request.body)
    ajax_username = data.get('username')
    targetuser = auth_views.UserModel.objects.get(username=ajax_username)
    
    # 회원가입이 가능한 ID인 경우:
    if targetuser.username != ajax_username:
        return JsonResponse({'result': 'True'})
    # 회원가입이 불가능한 ID인 경우:
    else:
        return JsonResponse({'result': 'False'})

# # 원본 ajax login view 함수
def ajax_user_login(request):
    data = loads(request.body)
    ajax_username = data.get('username')
    ajax_password = data.get('password')
    targetuser = auth_views.UserModel.objects.get(username=ajax_username)

    # 로그인 시 입력한 ID가 데이터베이스에 존재하지만 PW가 일치하지 않아 로그인이 되지 않는 경우.
    if targetuser.set_password != ajax_password:
        return JsonResponse({'result': 'False'})
    # 로그인 시 입력한 ID가 데이터베이스에 존재하지않는 경우 로그인이 되는 경우.
    else:
        return JsonResponse({'result': 'True'})

#####테스트중
# def ajax_user_login(request):
#     data = loads(request.body)
#     ajax_username = data.get('username')
#     ajax_password = data.get('password')
#     targetuser = auth_views.UserModel.objects.get(username=ajax_username)

#     if ajax_username is None:
#         return JsonResponse({'result': 'UserNameNone'})
#     elif ajax_password is None:
#         return JsonResponse({'result': 'UserPassNone'})
#     elif ajax_username =!

#     elif targetuser.set_password != ajax_password:
#         return JsonResponse({'result': 'InvalidPw'})
#     else:
#         return JsonResponse({'result': 'True'})


    # # 로그인 시 입력한 ID가 데이터베이스에 존재하지만 PW가 일치하지 않아 로그인이 되지 않는 경우.
    # if targetuser.set_password != ajax_password:
    #     return JsonResponse({'result': 'False'})
    # # 로그인 시 입력한 ID가 데이터베이스에 존재하지않는 경우 로그인이 되는 경우.
    # else:
    #     return JsonResponse({'result': 'True'})
##############

class UserLoginView(LoginView):
    template_name = 'dist/index.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)
    

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

# def login(request):
#     return render(request, 'dist/index.html')
# 로그인할때 사용하는 클래스 함수.
# 로그인 이후 넘어가는 화면은 settings.py 의 Login_redirect_url

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


# 유저가 선택한 데이터가 있는 게시판을 만들기 위한 view
class UserSelectedDataView(generic.ListView):
    model = SelectedBase
    paginate_by = 12
    template_name = 'user/user_selected_data.html'
    context_object_name = "selecteddata_list"

    

