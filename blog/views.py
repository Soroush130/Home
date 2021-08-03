from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from blog.forms import CommentForm, ReplyCommentForm
from blog.models import Blog, Comment
from django.contrib.auth.decorators import login_required


class HomeList(ListView):
    template_name = 'blog_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Blog.objects.get_active_blog()


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    comment_form = CommentForm()
    reply_comment_form = ReplyCommentForm()
    comments = Comment.objects.filter(blog_id=blog)
    context = {
        'blog': blog,
        'comment_form': comment_form,
        'comments': comments,
        'reply_comment_form': reply_comment_form,
    }
    return render(request, 'blog_detail.html', context)


@login_required(login_url='/login')
def product_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            Comment.objects.create(comment=data['comment'], rate=data['rate'], user_id=request.user.id, blog_id=id,
                                   is_reply=False)
            return redirect(url)


@login_required(login_url='/login')
def product_replycomment(request, id, comment_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form_reply_comment = ReplyCommentForm(request.POST)
        if form_reply_comment.is_valid():
            data = form_reply_comment.cleaned_data
            Comment.objects.create(comment=data['comment'], blog_id=id, user_id=request.user.id, reply_id=comment_id,
                                   is_reply=True)
            return redirect(url)
