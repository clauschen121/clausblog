from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.


def index(request):
    article_list = Article.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'article_list': article_list})


def article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article.html', context={'article': article})
