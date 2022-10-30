from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 20 # пагинация

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Shpargalka'
        return context

class PostByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 20# пагинация
    allow_empty = False # ошибка при запросе пустой категории

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


def index(request):
    return render(request, 'blog/index.html')

def get_category(request, slug):
    return render(request, 'blog/category.html')

def get_post(request, slug):
    return render(request, 'blog/category.html')


