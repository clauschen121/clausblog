from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from comments.forms import CommentForm
import markdown


# Create your views here.


def index(request):
    article_list = Article.objects.all()
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })


def article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.increase_views()
    article.body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    form = CommentForm()
    comment_list = article.comment_set.all()
    context = {
        'article': article,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, 'blog/article.html', context=context)


def archives(request, year, month):
    article_list = Article.objects.filter(
        created_time__year=year,
        created_time__month=month
    )
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(
        category=cate)
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })
