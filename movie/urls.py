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
    # path('<int:user_id>/board/1/S', views.MovieBoard1SelectCreateView.as_view(), name= 'board1S'), ## 클래스뷰로하려는안되서 함수형뷰사용해보려함.
    path('<int:user_id>/board/1/S', views.movieboardselectview, name= 'board1S'),  ## 함수형뷰 테스트
    # path('<int:movie_id>/board/1/S', views.MovieBoard1SelectDetailView.as_view(), name= 'board1S'),
    path('board/2', views.MovieBoardGenre.as_view(), name='board2'),
    path('board/3', views.MovieBoardActor.as_view(), name='board3'),
    path('board/4',views.MovieBoardtest ,name='board4'),
]
