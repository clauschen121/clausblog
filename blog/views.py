from django.shortcuts import get_object_or_404
from .models import Article, Category, Tag
from comments.forms import CommentForm
import markdown
from django.views.generic import ListView, DetailView
from MyUser.models import UserProfile


# Create your views here.

'''
def index(request):
    article_list = Article.objects.all()
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })
'''


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = self.pagination_data(paginator, page, is_paginated)

        context.update(pagination_data)

        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}
        left = []
        right = []
        left_has_more = False
        right_has_more = False

        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages

        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[
                (page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[
                (page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last
        }

        return data


'''
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
'''


class ArticleView(DetailView):
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'

    def get(self, request, *args, **kwargs):
        response = super(ArticleView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        article = super(ArticleView, self).get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        article.body = md.convert(article.body)
        article.toc = md.toc
        return article

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        pre_article = self.get_pre_article()
        next_article = self.get_next_article()
        context.update({
            'form': form,
            'comment_list': comment_list,
            'pre_article': pre_article,
            'next_article': next_article,
        })
        return context

    def get_pre_article(self):
        pre_article = Article.objects.filter(
            id__gt=self.kwargs.get('pk')).order_by('id')
        if pre_article.count() > 0:
            pre_article = pre_article[0]
        else:
            pre_article = None
        return pre_article

    def get_next_article(self):
        next_article = Article.objects.filter(
            id__lt=self.kwargs.get('pk')).order_by('-id')
        if next_article.count() > 0:
            next_article = next_article[0]
        else:
            next_article = None
        return next_article


'''
def archives(request, year, month):
    article_list = Article.objects.filter(
        created_time__year=year,
        created_time__month=month
    )
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })
'''


class ArchivesView(IndexView):

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(
            created_time__year=year,
            created_time__month=month
        )


'''
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(
        category=cate)
    return render(request, 'blog/index.html', context={
        'article_list': article_list
    })
'''


class CategoryView(IndexView):

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class TagView(IndexView):

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)


class AuthorView(IndexView):

    def get_queryset(self):
        author = get_object_or_404(UserProfile, pk=self.kwargs.get('pk'))
        return super(AuthorView, self).get_queryset().filter(author=author)
