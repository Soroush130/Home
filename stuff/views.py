from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from stuff.models import Stuff


class stuff_page(ListView):
    template_name = 'stuff.html'
    paginate_by = 6

    def get_queryset(self):
        return Stuff.objects.all()


def stuff_detail(request, id):
    stuff = Stuff.objects.get(id=id)
    projects_stuff = stuff.stuff.all()
    context = {
        'stuff': stuff,
        'projects_stuff': projects_stuff,
    }
    return render(request, 'stuff-detail.html', context)


class SearchStuffView(ListView):
    template_name = 'home.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        # print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Stuff.objects.search(query)

        return Stuff.objects.all()

