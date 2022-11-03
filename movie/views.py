from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from movie.models import TargetBase, SelectedBase, Actorlist
from movie.models import TargetBase, Actorlist
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SelectedBaseForm
from .models import SelectedBase
from django.contrib.auth import views as auth_views
@login_required(login_url=reverse_lazy('user:login'))
def MovieBoardtest(request):
    """ClassView를 사용하기전 임시로 사용하는 view함수"""
    return render(request, 'movie/main.html')
    
@login_required(login_url=reverse_lazy('user:login'))
def select(request):
    """선택/검색 임시"""
    return render(request, 'movie/select.html')

class SelectCreateView(LoginRequiredMixin ,generic.CreateView):
    model = TargetBase
    fields = ['nations', 'audit']
    template_name = 'movie/main.html'
    login_url = reverse_lazy('user:login')

    def form_valid(self, form):
        print(form.instance)
        print(form.cleaned_data)
        # print(form.cleaned_data['openDt2'])
        form.instance.moviebase_id = self.request.user.id
        form.save()
        return redirect(reverse_lazy('movie:selectlist'))
    
    def form_invalid(self, form):
        print("유효하지 않은 폼 데이터")
        print(form.instance)
        print(form.cleaned_data)
        return super().form_invalid(form)

class SelectListView(generic.ListView):
    model = TargetBase
    template_name = 'movie/result.html'

class SelectDetailView(generic.DetailView):
    pass


# class MovieBoard(generic.ListView):
#     model: Optional[Type[Model]]

# @login_required(login_url=reverse_lazy('user:login'))
class MovieBoardtest1(generic.ListView):

    # model = TargetBase
    paginate_by = 12
    template_name = "movie/main1.html"
    # queryset = TargetBase.objects.values('director').distinct()
    context_object_name = "targetbase_list"

    # 검색창에서 검색한 내용을 띄어주기 위한것
    def get_queryset(self):
        search_word = self.request.GET.get('searchWord','')
        if search_word:
            result = TargetBase.objects.values('director').distinct().filter(director__contains=search_word)
        else:
            result = TargetBase.objects.values('director').distinct()            
        return result
    
    # 요청을 통해 전달받은 검색어를 다시 템플릿으로 전달
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_word = self.request.GET.get('searchWord','')
        if search_word:
            context['searchWord'] = search_word
        return context

    # def get_queryset(self):
    #     return TargetBase.objects.distinct().values_list('director')

# def testboard(request):
#     posts = TargetBase.objects.all()
#     return render(request, 'movie/main1.html', {"posts": posts})

# class MovieBoard1SelectDetailView(generic.DetailView):
#     model = SelectedBase
#     template_name = 'movie/result.html'
#     # context_object_name: str
#     pk_url_kwarg = 'movie_id'

class MovieBoard1SelectCreateView(LoginRequiredMixin, generic.CreateView):    
    model = SelectedBase
    template_name = 'movie/result.html'
    fields = ['director']
    success_url = '/'
    pk_url_kwarg = 'user_id'
    login_url = reverse_lazy('user:login')
    # form_class = SelectedBaseForm

def movieboardselectview(request, user_id):
    request.session['selected_director']= request.GET['director']
    target = request.GET.get('director','') 
    user = auth_views.UserModel.objects.get(pk=user_id)
    SelectedBase.objects.create(director=target, writer_id=user.id)
    return render(request, 'movie/result.html')
   
# 메인페이지2. 장르 선택 페이지를 보여주기 위한 클래스뷰
# classview에서 login_required쓰면 오류가 났었던것 같았음
# @login_required(login_url=reverse_lazy('user:login'))
class MovieBoardGenre(generic.ListView):

    # 페이징 수
    paginate_by = 12
    # 연결할 템플릿 이름
    template_name = "movie/main2.html"
    # 장고 템플릿에서 사용할 변수 이름
    context_object_name = "targetbase_list"

    # 검색창에서 검색한 내용을 아래에 띄어주기 위한 것
    def get_queryset(self):
        search_word = self.request.GET.get('searchWord', '')
        if search_word:
            result = TargetBase.objects.values('genre').distinct().filter(genre__contains=search_word)
        else:
            result = TargetBase.objects.values('genre').distinct()
        return result
    
    # 요청을 통해 전달받은 검색어를 다시 템플릿으로 전달
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_word = self.request.GET.get('searchWord','')
        selected_genre = self.request.GET.get('selected_genre', '')
        if search_word:
            context['searchWord'] = search_word
        context['selected_genre'] = selected_genre
        return context
   
# 메인페이지3. 배우 선택 페이지를 보여주기 위한 클래스뷰
class MovieBoardActor(generic.ListView):

    # 페이징 수
    paginate_by = 12
    # 연결할 템플릿 이름
    template_name = "movie/main3.html"
    # 장고 템플릿에서 사용할 변수 이름
    context_object_name = "actorlist_list"

    # 검색창에서 검색한 내용을 아래에 띄어주기 위한 것
    def get_queryset(self):
        search_word = self.request.GET.get('searchWord','')
        if search_word:
            result = Actorlist.objects.values('actor1').filter(actor1__contains=search_word)
        else:
            result = Actorlist.objects.values('actor1')
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_word = self.request.GET.get('searchWord','')
        selected_actor1 = self.request.GET.get('selected_actor1','')
        selected_actor2 = self.request.GET.get('selected_actor2','')
        selected_actor3 = self.request.GET.get('selected_actor3','')
        print(search_word, selected_actor1, selected_actor2, selected_actor3)
        if search_word:
            context['searchWord'] = search_word
        context['selected_actor1'] = selected_actor1
        context['selected_actor2'] = selected_actor2
        context['selected_actor3'] = selected_actor3
        return context
