from django.urls import path
from . import views
app_name = 'movie'
urlpatterns = [
    # path('board/',views.MovieBoard ,name='board'),
    path('board/',views.MovieBoardtest ,name='board'),
]
