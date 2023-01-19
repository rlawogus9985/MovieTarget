from django.shortcuts import render, redirect
from django.views import generic
from json import loads
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from movie.models import TargetBase, SelectedBase, Actorlist
from movie.models import TargetBase, Actorlist, Secondbase
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SelectedBaseForm
from .models import SelectedBase
from django.contrib.auth import views as auth_views
from django.http import JsonResponse
import joblib
import pandas as pd
@login_required(login_url=reverse_lazy('user:login'))
def MovieBoardtest(request):
    """
    [ClassView를 사용하기전 임시로 사용하는 view함수 => 프로젝트초기의설명] 
    초기에 만들었던 함수로써 관련된 html명의 수정이 필요함,
    현재에는 path.name의 board4을 출력하는 역할을 하는 함수뷰
    """
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

# board1의 감독선택을 위한 ListView
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
            result = TargetBase.objects.values('director').distinct().filter(director__icontains=search_word)
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

############ 

# 세션저장을위한 징검다리 역할을 하는 url들의 함수뷰들

def director_to_genre(request):
    """ board1의 form에서 director라는 name을 가진 데이터를 받아 세션에 저장하고 다음페이지인 board2로 redirect하는 함수뷰"""
    targetdirector = request.GET.get('director','')
    request.session['selected_director']= targetdirector
    return redirect(reverse('movie:board2'))

def genre_to_actor(request):
    """ board2의 form에서 genre라는 name을 가진 데이터를 받아 세션에 저장하고 다음페이지인 board3로 redirect하는 함수뷰"""
    targetgenre = request.GET.get('genre','')
    request.session['selected_genre']= targetgenre
    return redirect(reverse('movie:board3'))

def actor_to_nations_opendt_audit(request):
    """ board3의 form에서 actor1~3의 name을 가진 데이터를 받아 세션에 저장하고 다음페이지인 board4로 redirect하는 함수뷰"""
    targetactor1 = request.GET.get('actor1', '')
    targetactor2 = request.GET.get('actor2', '')
    targetactor3 = request.GET.get('actor3', '')
    request.session['selected_actor1'] = targetactor1
    request.session['selected_actor2'] = targetactor2
    request.session['selected_actor3'] = targetactor3
    return redirect(reverse('movie:board4'))

def nations_opendt_audit_to_result(request):
    """
    boar4의 form에서 nations, opendt, audit의 name을 가진 데이터를 받아 세션에 저장하고,
    다음페이지인 [app_name : movie / pathname " board1S 의 url의 result.html을 향한 render에]  redirect하는 함수뷰
    pathname이나 해당 html 밑 url명 통일성을위한 향후 수정이 필요함.
    """
    targetnations = request.GET.get('nations', '')
    targetopendt = request.GET.get('opendt', '')
    targetaudit = request.GET.get('audit', '')
    request.session['selected_nations'] = targetnations
    request.session['selected_opendt'] = targetopendt
    request.session['selected_audit'] = targetaudit
    return redirect(reverse('movie:board1S'))

###########

# 정상적으로 감독,장르,배우,...를 선택해서 결과페이지에 들어가면 session에 있는 정보를
# 데이터베이스에 저장해서 그 데이터베이스를 html에 넘겨준다.
def movieboardselectview(request):
    # targetdirector = request.GET.get('director','') 
    # targetgenre = request.GET.get('genre', '')
    # targetnations = request.GET.get('nations', '')
    # targetaudit = request.GET.get('audit', '')
    # targetactor1 = request.GET.get('actor1', '')
    # targetactor2 = request.GET.get('actor2', '')
    # targetactor3 = request.GET.get('actor3', '')
    # targetopendt = request.GET.get('opendt', '')
    movie = None
    try:
        targetdirector = request.session['selected_director']
        targetgenre = request.session['selected_genre']
        targetactor1 = request.session['selected_actor1']
        targetactor2 = request.session['selected_actor2']
        targetactor3 = request.session['selected_actor3']
        targetnations = request.session['selected_nations'] 
        targetopendt = request.session['selected_opendt']
        targetaudit = request.session['selected_audit']
        userid = request.user.id

        movie = SelectedBase.objects.create(
        writer_id=userid, director=targetdirector, genre=targetgenre,
        actor1=targetactor1, actor2=targetactor2, actor3=targetactor3,
        nations=targetnations, audit=targetaudit,  opendt=targetopendt)
    except:
        pass
   
    context = {
        'movie': movie,
    }
    # user = auth_views.UserModel.objects.get(pk=pk)
    return render(request, 'movie/result.html', context)

# 자료실에서 결과보기를 누르면 pk에 맞춰서 그 정보를 넘겨준다.
class movieboardputview(generic.DetailView):
    model = SelectedBase
    template_name = 'movie/result.html'
    context_object_name = 'movie'
    def get_queryset(self):
        pk = self.kwargs.get('pk')

        result = SelectedBase.objects.filter(pk=pk)
        return result
    
def delete_board(request, pk):
    board = SelectedBase.objects.get(pk=pk)
    board.delete()
    return redirect(reverse('user:selected_data'))


# class NationsOpendtAuditToResult(generic.CreateView):

#     pk_url_kwarg = 'user_id'

#     def get_queryset(self, request, user_id):
#         targetdirector = request.session['selected_director']
#         targetgenre = request.session['selected_genre']
#         targetactor1 = request.session['selected_actor1']
#         targetactor2 = request.session['selected_actor2']
#         targetactor3 = request.session['selected_actor3']
#         targetnations = request.session['selected_nations'] 
#         targetopendt = request.session['selected_opendt']
#         targetaudit = request.session['selected_audit']

#         # user = auth_views.UserModel.objects.get(pk=user_id)
#         SelectedBase.objects.create(writer_id=user_id, director=targetdirector, genre=targetgenre,
#         actor1=targetactor1, actor2=targetactor2, actor3=targetactor3,
#         nations=targetnations, audit=targetaudit,  opendt=targetopendt)
#         return render(request, 'movie/result.html')



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
            result = TargetBase.objects.values('genre').distinct().filter(genre__icontains=search_word)
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
            result = Actorlist.objects.values('actor1').filter(actor1__icontains=search_word)
        else:
            result = Actorlist.objects.values('actor1')
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_word = self.request.GET.get('searchWord','')
        selected_actor1 = self.request.GET.get('selected_actor1','')
        selected_actor2 = self.request.GET.get('selected_actor2','')
        selected_actor3 = self.request.GET.get('selected_actor3','')
        # print(search_word, selected_actor1, selected_actor2, selected_actor3)
        if search_word:
            context['searchWord'] = search_word
        context['selected_actor1'] = selected_actor1
        context['selected_actor2'] = selected_actor2
        context['selected_actor3'] = selected_actor3
        return context

loaded_model = joblib.load('model/sim_model.pkl')
# print(loaded_model)
# 영화 추천 페이지에 대한 class view
class recommendation(generic.ListView):
    template_name = 'movie/recommendation.html'
    context_object_name = 'targetbase'

    global loaded_model
    def get_queryset(self):
        # 검색어는 정확히 일치해야한다.
        search_word = self.request.GET.get('searchWord','')

        sort_criteria = self.request.GET.get('criteria','')
        search_word2 = self.request.GET.get('searchWord2','')
        print(sort_criteria)
        qs = Secondbase.objects.all().values()
        data = pd.DataFrame(qs)
        result = []
        if search_word or search_word2:
            if search_word:
                diction = find_sim_movie(data,loaded_model,search_word,11).to_dict()
            if search_word2:
                diction = find_sim_movie(data,loaded_model,search_word2,11).to_dict()
            for i in zip(diction['index'].values() ,diction['id'].values(),diction['release_date'].values(),diction['title'].values(),diction['director'].values(),diction['genres'].values(),
                diction['original_language'].values(),diction['overview'].values(),diction['popularity'].values(),diction['budget'].values(),diction['revenue'].values(),diction['tagline'].values(),diction['vote_average'].values(),diction['vote_count'].values(),diction['credits'].values(),
                diction['keywords'].values(),diction['poster_path'].values(),diction['audits'].values()):
                result.append({ x:y for x,y in zip(diction.keys(),i)})
            # result = Secondbase.objects.filter(title=search_word)
            # print(result)
        else:
            result = None
        print(f'{search_word=}, {sort_criteria=}, {search_word2=}')
        # result 리스트가 만들어진 상태에서 진행.
        if sort_criteria == '유사도 내림차순':
            result = result
        elif sort_criteria == '유사도 오름차순':
            searched = result[0]
            result.pop(0)
            sorted_by_similarity_asc = list(reversed(result))
            sorted_by_similarity_asc.insert(0, searched)
            result = sorted_by_similarity_asc
        elif sort_criteria == '평점 내림차순':
            searched = result[0]
            result.pop(0)
            sorted_by_vote_desc = list(reversed(sorted(result, key=lambda x: x['vote_average'])))
            sorted_by_vote_desc.insert(0, searched)
            result = sorted_by_vote_desc
        elif sort_criteria == '평점 오름차순':
            searched = result[0]
            result.pop(0)
            sorted_by_vote_asc = list(sorted(result, key=lambda x: x['vote_average']))
            sorted_by_vote_asc.insert(0, searched)
            result = sorted_by_vote_asc
        elif sort_criteria == '상영일 내림차순':
            searched = result[0]
            result.pop(0)
            sorted_by_release_date_desc = list(reversed(sorted(result, key=lambda x:x['release_date'])))
            sorted_by_release_date_desc.insert(0, searched)
            result = sorted_by_release_date_desc
        elif sort_criteria == '상영일 오름차순':
            searched = result[0]
            result.pop(0)
            sorted_by_release_date_asc = list(sorted(result, key=lambda x: x['release_date']))
            sorted_by_release_date_asc.insert(0, searched)
            result = sorted_by_release_date_asc

        return result
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_word = self.request.GET.get('searchWord','')
        search_word2 = self.request.GET.get('searchWord2','')
        option = self.request.GET.get('criteria','유사도 내림차순')
        if search_word:
            context['searchWord'] = search_word
            context['optionWord'] = option
        if search_word2:
            context['searchWord'] = search_word2
            context['optionWord'] = option
        return context
        
    
def find_sim_movie(df, sorted_idx, title_name, top_n=10):
    target_movie = df[df['title'] == title_name][:1]

    title_index = target_movie.index.values
    similar_index = sorted_idx[title_index, :top_n]
    similar_index = similar_index.reshape(-1)

    return df.iloc[similar_index]



# ajax로 자동완성을 위해 받아오기 위한 함수
def recomAjax(request):
    input_val = request.GET.get('searchTitle','')
    
    result = Secondbase.objects.values('title').filter(title__icontains=input_val)
    context = { 'result_title': result}
    print(input_val)
    return render(request, 'movie/recommendation.html',context)
    # return JsonResponse(context)
    
