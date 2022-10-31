from unittest.loader import VALID_MODULE_NAME
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from movie.models import TargetBase
from django.contrib.auth.mixins import LoginRequiredMixin


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
    queryset = TargetBase.objects.values('director').distinct()
    context_object_name = "targetbase_list"
    
    # def get_queryset(self):
    #     return TargetBase.objects.distinct().values_list('director')

# def testboard(request):
#     posts = TargetBase.objects.all()
#     return render(request, 'movie/main1.html', {"posts": posts})

