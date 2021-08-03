import itertools

from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from homes.forms import MessageForm
from homes.models import Home, HomeGallery, Message, Variant


class HomeList(ListView):
    template_name = 'home.html'
    paginate_by = 6

    def get_queryset(self):
        return Home.objects.all()


# def home_list(request):
#     homes = Home.objects.all()[:6]
#     context = {
#         'homes': homes
#     }
#     return render(request, 'home.html', context)


# amenities == به معنی آپشن ها در اینجا استفاده می شود

def home_detail(request, id):
    url = request.META.get('HTTP_REFERER')
    # form = MessageForm()
    home = Home.objects.get(id=id)
    galleries = HomeGallery.objects.filter(home_id=home)
    amenities = home.amenities.all()
    variant = Variant.objects.get(home_id=home)
    if request.method == "POST":
        form_message = MessageForm(request.POST)
        if form_message.is_valid():
            data = form_message.cleaned_data
            message = Message.objects.create(stuff_id=home.stuff.id, name=data['name'], email=['email'], text=['text'])
            message.save()
            return redirect(url)
    else:
        form_message = MessageForm()

    context = {
        'home': home,
        'variant': variant,
        'galleries': galleries,
        'amenities': amenities,
        'form_message': form_message,
    }
    return render(request, 'home_detail.html', context)


class SearchHomesView(ListView):
    template_name = 'home.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Home.objects.search(query)

        return Home.objects.all()


