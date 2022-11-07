from django.urls import path
from . import views
app_name = 'movie'
urlpatterns = [
    
    path('board/1', views.MovieBoardtest1.as_view(), name='board1'),
    path('board/1to2/', views.director_to_genre, name='board1to2'),
    path('board/2', views.MovieBoardGenre.as_view(), name='board2'),
    path('board/2to3/', views.genre_to_actor, name='board2to3'),
    path('board/3', views.MovieBoardActor.as_view(), name='board3'),
    path('board/3to4/', views.actor_to_nations_opendt_audit, name='board3to4'),
    path('board/4',views.MovieBoardtest ,name='board4'),

    path('board/board4toresult', views.nations_opendt_audit_to_result, name='board4toresult'), ##원래 사용하는 함수뷰
    # path('select/',views.SelectCreateView.as_view(), name='select'),
    # path('board/board4toresult', views.NationsOpendtAuditToResult.as_view(), name='board4toresult'),  ## 시도중인 클래스뷰
        ## class뷰에 generic.ListView를 상속받아 저장되어있는 세션을 이용한 쿼리문 작성을 시도하였으나,
        ## class뷰에는 함수형뷰의 request 매개변수가 없어서 request인수에서 session을 불러오는게 어려워보인다.
        ## class view django session으로 구글에 검색시 맨 처음 나오는 영어질문에 답이 있는것 같으나, override가 복잡하고 이해하지 못해서 작업중지한 상황.
    
    path('board/1/S', views.movieboardselectview, name= 'board1S'),  
        ## 함수형뷰 테스트였었던 url로 session들을 뽑아낼 result 결과페이지를 연결하는 url

    ####### 기준선으로 위 urlpattern은 사용 / 아래 urlpattern은 비사용 ###########

    # path('board/',views.MovieBoard ,name='board'), 
    # path('select/', views.select, name='select'),
    # path('selectlist/', views.SelectListView.as_view(), name='selectlist'),
    # path('selectdetail/', views.SelectDetailView.as_view(), name='selectdetail'),
    # path('<int:user_id>/board/1/S', views.MovieBoard1SelectCreateView.as_view(), name= 'board1S'), ## 클래스뷰로하려는안되서 함수형뷰사용해보려함.
    # path('<int:movie_id>/board/1/S', views.MovieBoard1SelectDetailView.as_view(), name= 'board1S'),
    
]
