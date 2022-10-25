from django.shortcuts import render
from django.views import generic
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy

class UserCreateForm(generic.CreateView):
    form_class = auth_forms.UserCreationForm
    template_name = 'dist/index.html' # get 방식일 경우 회원가입유도
    success_url = reverse_lazy('user:login') # post 방식일 경우 리다이렉트로 로그인으로 가는상황


# Create your views here.
def login(request):
    return render(request, 'dist/index.html')
