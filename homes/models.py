import os
from django.db import models
from django.db.models import Q
from stuff.models import Stuff


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"HOME/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"HOME/{final_name}"


class HomeType(models.Model):
    title = models.CharField(max_length=250, verbose_name='نوع ساختمان')

    class Meta:
        verbose_name_plural = 'HomeType'

    def __str__(self):
        return self.title


class Amenities(models.Model):
    title = models.CharField(max_length=150, verbose_name='آپشن ها')

    class Meta:
        verbose_name = 'amenities'
        verbose_name_plural = 'Amenities'

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=150, verbose_name='شهر')

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'City'

    def __str__(self):
        return self.title


class HomesManager(models.Manager):

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query)
        )
        return self.get_queryset().filter(lookup).distinct()


class Home(models.Model):
    VARIANT = (
        ('Sale', 'sale'),
        ('Mortgage', 'mortgage'),
        ('Rent', 'rent'),
        ('Mortgage And Rent', 'mortgage and rent'),
    )
    title = models.CharField(max_length=200, verbose_name='نام ساختمان')
    city = models.ForeignKey(City, related_name='city', on_delete=models.CASCADE, max_length=100, verbose_name='شهر',
                             default=None)
    area = models.IntegerField(verbose_name='متراژ')
    bedroom = models.IntegerField(verbose_name='تعداد اتاق خواب')
    baths = models.IntegerField(verbose_name='تعداد سرویس / حمام')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیخات', null=True, blank=True)
    location = models.CharField(max_length=250, verbose_name='آدرس')
    home_type = models.OneToOneField(HomeType, verbose_name='نوع ساختمان', related_name="amenities",
                                     on_delete=models.CASCADE, default=None)
    status = models.CharField(max_length=100, verbose_name='وضیعت', choices=VARIANT)
    # price = models.IntegerField(verbose_name='قیمت')
    garage = models.IntegerField(verbose_name='تعداد گاراژ')
    amenities = models.ManyToManyField(Amenities, verbose_name="آپشن ها", related_name='amenities')
    stuff = models.ForeignKey(Stuff, verbose_name='مشاور', on_delete=models.CASCADE,
                              related_name='stuff', null=True, blank=True)

    objects = HomesManager()

    class Meta:
        verbose_name = 'home'
        verbose_name_plural = 'HOMES'

    def __str__(self):
        return self.title


class HomeGallery(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام عکس')
    image = models.ImageField(upload_to=upload_gallery_image_path, null=True, blank=True, verbose_name='تصویر')
    home = models.ForeignKey(Home, on_delete=models.CASCADE, verbose_name='ساختمان', default=None)

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.title


class Message(models.Model):
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE, related_name="message_stuff")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name


class Variant(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='hr')
    price_sale = models.IntegerField(null=True, blank=True)
    price_mortgage = models.IntegerField(null=True, blank=True)
    price_rent = models.IntegerField(null=True, blank=True)
    mortgage_rent = models.BooleanField(default=False, verbose_name="آیا رهن و اجاره است ؟")

    def __str__(self):
        return self.home.title
