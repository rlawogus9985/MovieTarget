from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import forms as auth_forms

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import CheckPasswordForm


from user.decorators import * # 함수형 뷰 데코
# from django.utils.decorators import method_decorator # 클래스기반뷰에사용 데코
# from django.contrib.auth.decorators import login_required # django 내장 데코


class UserCreateForm(generic.CreateView):
    form_class = auth_forms.UserCreationForm
    template_name = 'dist/index.html' # get 방식일 경우 회원가입유도
    success_url = reverse_lazy('user:login') # post 방식일 경우 리다이렉트로 로그인으로 가는상황


def login(request):
    return render(request, 'dist/index.html')

def profile(request):
    return render(request, 'user/profile.html')


def delete_user_page(request):
    return render(request, 'user/user_delete.html')

@require_POST
@login_required
def delete_user(request):
    request.user.delete()
    return redirect('user:join')


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

