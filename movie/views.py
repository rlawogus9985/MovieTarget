from django.shortcuts import render, redirect
from django.views import generic


def MovieBoardtest(request):
    """ClassView를 사용하기전 임시로 사용하는 view함수"""
    return render(request, 'movie/main.html')

# class MovieBoard(generic.ListView):
#     model: Optional[Type[Model]]