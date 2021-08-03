from django.contrib import admin
from django.urls import path, include

from blog.views import HomeList, blog_detail, product_comment, product_replycomment

urlpatterns = [
    path("blog-list", HomeList.as_view()),
    path("blogs/<int:id>", blog_detail),

    path('comment/<int:id>', product_comment),
    path('reply-comment/<int:id>/<int:comment_id>', product_replycomment),
]

