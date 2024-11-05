from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from Ninte_APP.forms import PostForm
from Ninte_APP.models import Post


# Create your views here.


# базовый класс для представлений

class MainPage(View):

    def get(self, request):
        return render(request, 'Ninte_APP/main.html')

    def post(self, request):
        print('hello post')
        return render(request, 'Ninte_APP/main.html')


# class TemplateView является представлением отрисовки html

# @method_decorator(login_required) #указывание декораторов для классов
class MainView2(TemplateView):
    template_name = 'Ninte_APP/main.html'

    # передача контекста когда данные в виде текста хранятся либо же строго определенные значения
    extra_context = {'title': 'Hello Template View!'}


    # передача контекста когда данные в виде словаря
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tit'] = ' Template View!'
        return context


class PostListView(ListView):
    model = Post
    template_name = 'Ninte_APP/post_list.html'
    context_object_name = 'posts' # передача названия переменной в шаблон
    paginate_by = 2   # пагинация скок элемента отображать на странице
    # extra_context = {
    #
    # }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Posts' дополнительные контексты так передаются в шаблон в квадратных скобках пишем как хотим передать а потом что именно мы получаем
        print(context)
        return context

    # получение списка постов из queryset тут мы переопределяем и получаем только публикованные посты (это пример)
    def get_queryset(self):
        return Post.objects.filter(is_published=False)

# отображение полной информации о определенном посте
class PostDetailView(DetailView):
    model = Post
    template_name = 'Ninte_APP/post_detail.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'Ninte_APP/post_create.html'
    success_url = reverse_lazy('post_list') # переход на страницу что бы указать name нашей url надо вызвать функцию reverse_lazy
    def form_valid(self, form):
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'Ninte_APP/post_update.html'
    success_url = reverse_lazy('post_list') # переход на страницу что бы указать name нашей url надо вызвать функцию reverse_lazy


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'Ninte_APP/post_create.html'
    success_url = reverse_lazy('post_list')

