from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

@login_required(login_url=reverse_lazy('user:login'))
def MovieBoardtest(request):
    """ClassView를 사용하기전 임시로 사용하는 view함수"""
    return render(request, 'movie/main.html')
    
@login_required(login_url=reverse_lazy('user:login'))
def select(request):
    """선택/검색 임시"""
    return render(request, 'movie/select.html')

# class MovieBoard(generic.ListView):
#     model: Optional[Type[Model]]