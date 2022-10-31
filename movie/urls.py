from django.urls import path
from . import views
app_name = 'movie'
urlpatterns = [
    # path('board/',views.MovieBoard ,name='board'), 
    # path('select/', views.select, name='select'),
    path('select/',views.SelectCreateView.as_view(), name='select'),
    path('slectlist/', views.SelectListView.as_view(), name='selectlist'),
    path('selectdetail/', views.SelectDetailView.as_view(), name='selectdetail'),
    path('board/1', views.MovieBoardtest1.as_view(), name='board1'),
    path('board/4',views.MovieBoardtest ,name='board4'),
]
