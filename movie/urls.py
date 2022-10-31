from django.urls import path
from . import views
app_name = 'movie'
urlpatterns = [
    # path('board/',views.MovieBoard ,name='board'),
    path('board/',views.MovieBoardtest ,name='board'),
    # path('select/', views.select, name='select'),
    path('select/',views.SelectCreateView.as_view(), name='select'),
    path('slectlist/', views.SelectListView.as_view(), name='selectlist'),
    path('selectdetail/', views.SelectDetailView.as_view(), name='selectdetail'),
]
