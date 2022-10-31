from django.urls import path
from . import views
app_name = 'movie'
urlpatterns = [
    # path('board/',views.MovieBoard ,name='board'),
    path('board/1', views.MovieBoardtest1.as_view(), name='board1'),
    path('board/4',views.MovieBoardtest ,name='board4'),
    path('select/', views.select, name='select'),
]
