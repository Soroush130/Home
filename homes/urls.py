from django.urls import path, include

from homes.views import home_detail, HomeList, SearchHomesView

urlpatterns = [
    path('homes', HomeList.as_view()),
    # path('homes', home_list),
    path('homes/<int:id>', home_detail),
    path('home/search', SearchHomesView.as_view()),
]

