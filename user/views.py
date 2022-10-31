from multiprocessing import context
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
    
    try:
        # authuserpk = auth_views.UserModel.objects.get(pk=auth_user_id)
        # authuserpk.password = password
        # auth_views.UserModel.save()
        auth_views.UserModel.objects.get(pk=auth_user_id).update(password=password)
        auth_views.UserModel.save()
    except:
        pass

    # AuthviewsUsermodel = auth_views.UserModel.objects.filter(pk=auth_user_id)  
    # AuthviewsUsermodel.objects.update(password=password)
    return redirect('user:profile')

#############################################
# @login_required
# @require_http_methods(['GET','POST'])
# def userchangeview(request):
#     if request.method == 'POST':
#         form = CustommUserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('user:profile')
#     else:
#         form = CustommUserChangeForm(instance=request.user)
#     context = {
#         'form':form,
#     }
#     return render(request, 'user/user_change_page.html', context)

####################################

# @login_required
# def userchangeview(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect('user:profile')         
#     else:
#         form = PasswordChangeForm(request.user)
#     context = {
#         'form' : form,
#     }
#     return render(request, 'user/user_change_page.html', context)


##############################################

# class UserChangeViews(generic.UpdateView):
#     models = auth_views.UserModel
#     context_object_name = 'password'
# #     form_class = auth_forms.UserChangeForm 
#     template_name = 'user/user_change_page.html'
#     success_url = reverse_lazy('movie:board') # post 방식일 경우 리다이렉트로 로그인으로 가는상황
# #     def get_queryset(self, auth_user_id):
# #         # changename = self.request.POST.get('changeName')

# #         originalname = self.request.POST.get('username')
# #         username = auth_views.UserModel.objects.username
        
# #         changepassword = self.request.POST.get('password')
# #         userid = auth_views.UserModel.objects.get(pk=auth_user_id)
        
# #         if originalname == username:
# #             auth_views.UserModel.objects.update('password' = changepassword)
            
# #         else:
# #             pass            

# #         if changepassword == auth_forms.UserModel.password and originalname == auth_forms.UserModel.username:
# #             auth_forms.UserModel.password = changepassword
# #         # return super().get_queryset()
# #         return 
#     @ login_required
#     def get_queryset(self, auth_user_id):
#         username = self.request.POST.get('username', '')
#         password = self.request.POST.get('password', '')
#         pk = self.kwargs.get('auth_user_id')
#         target = auth_views.UserModel.obejcts.get(pk=pk)
#         target.password = password
#         target.save()
#         return 
        
######################################################


@require_POST
@login_required(login_url=reverse_lazy('user:login'))
def delete_user(request):
    request.user.delete()
    return redirect('user:join')

# @login_required(login_url=reverse_lazy('user:login'))
# def delete_user(request):
#     if request.method == 'POST':
#         password_form = CheckPasswordForm(request.user, request.POST)
        
#         if password_form.is_valid():
#             request.user.delete()
#             logout(request)
#             messages.success(request, "회원탈퇴가 완료되었습니다.")
#             return redirect('/user/login/')
#     else:
#         password_form = CheckPasswordForm(request.user)

#     return render(request, 'user/user_delete.html', {'password_form':password_form})

