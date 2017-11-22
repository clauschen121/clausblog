from django.shortcuts import render, get_object_or_404
from .models import Article, Category
import markdown


# Create your views here.


def index(request):
    article_list = Article.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })


def article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return render(request, 'blog/article.html', context={'article': article})


def archives(request, year, month):
    article_list = Article.objects.filter(
        created_time__year=year,
        created_time__month=month
    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(
        category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })
