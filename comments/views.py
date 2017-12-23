from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from django.views.generic import ListView
from .models import Comment, Commentme
from .forms import CommentForm, CommentMeForm
import markdown

# Create your views here.


def article_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(article)
        else:
            # comment_list = article.comment_set.all()
            # context = {'article': article, 'form': form,
            #            'comment_list': comment_list}
            # return render(request, 'blog/article.html', context=context)
            return redirect(article)

    return redirect(article)


def commentmeadd(request):
    if request.method == 'POST':
        form = CommentMeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/comment/commentme/')
        else:
            return redirect('/comment/commentme/')
    return redirect('/comment/commentme/')


class CommentView(ListView):
    model = Commentme
    template_name = 'blog/comment.html'
    context_object_name = 'comment_list'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(CommentView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        form = CommentMeForm()

        pagination_data = self.pagination_data(paginator, page, is_paginated)
        count = Commentme.objects.count()
        context.update(pagination_data)
        context.update({
            'form': form,
            'count': count
        })
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        comment_list = context['comment_list']
        for comment in comment_list:
            comment.text = md.convert(comment.text)
        context.update({
            'comment_list': comment_list
        })

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
