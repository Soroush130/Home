import os

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"Blog/{final_name}"


class BlogManager(models.Manager):
    def get_active_blog(self):
        return self.get_queryset().filter(active=True)


class Ctegory(models.Model):
    title = models.CharField(max_length=150, verbose_name='نام دسته بندی')
    slug = models.SlugField(max_length=100, verbose_name="لینک")

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.CharField(max_length=150, verbose_name='توضیح کوتاه')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    body = models.TextField(verbose_name='توضیحات')
    author = models.ForeignKey(User, verbose_name='نویسنده', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="تاریخ انتشار", auto_now_add=True)
    active = models.BooleanField(verbose_name='فعال / غیر فعال', default=True)
    category = models.ForeignKey(Ctegory, verbose_name='دسته بندی', on_delete=models.CASCADE, related_name='category',
                                 default=None)
    objects = BlogManager()

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.PositiveIntegerField(default=1)
    create_on = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='reply_comment')
    is_reply = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
