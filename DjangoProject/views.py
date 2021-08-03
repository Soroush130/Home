import itertools
from django.shortcuts import render, HttpResponse, Http404

from blog.models import Blog
from homes.models import Home, HomeType, City
from stuff.models import Stuff
from .filters import HomeFilter


def header(request):
    home_type = HomeType.objects.all()
    city = City.objects.all()
    f = HomeFilter(request.GET, queryset=Home.objects.all())

    context = {
        'home_type': home_type,
        'city': city,
        'filter': f,
    }
    return render(request, 'shared/Header.html', context)


def footer(request):
    context = {}
    return render(request, 'shared/Footer.html', context)


def mygrouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    stuff = Stuff.objects.all()
    homes = Home.objects.all().order_by('-id')[:3]
    blogs = Blog.objects.all().order_by('-id')[:3]
    context = {
        'stuff': stuff,
        'homes': homes,
        'blogs': blogs,
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    stuff = Stuff.objects.all()
    context = {
        'stuff': stuff,
    }
    return render(request, 'about_page.html', context)


# ============ مربوط به سرچی که کاربر در قسمت هدر سایت انجام میدهد ==========
def search_header(request):
    f = HomeFilter(request.GET, queryset=Home.objects.all())
    context = {'filter': f}
    return render(request, 'index.html', context)
