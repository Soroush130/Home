import os

from django.db import models

# Create your models here.
from django.db.models import Q


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"stuff/{final_name}"


class StuffManager(models.Manager):

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query)
        )
        return self.get_queryset().filter(lookup).distinct()


class Stuff(models.Model):
    title = models.CharField(max_length=150, verbose_name='نام و نام خانوداگی')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیخات', null=True, blank=True)
    phone = models.IntegerField(verbose_name='شماره تلفن')
    email = models.EmailField(verbose_name='ایمیل')

    objects = StuffManager()

    class Meta:
        verbose_name = 'stuff'
        verbose_name_plural = 'Stuff'

    def __str__(self):
        return self.title
