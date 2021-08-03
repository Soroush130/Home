from django.contrib import admin
from django.urls import path, include

from stuff.views import stuff_page, stuff_detail, SearchStuffView

urlpatterns = [
    path('stuff-list', stuff_page.as_view()),
    path('stuff-list/<int:id>', stuff_detail),
    path('stuff/search', SearchStuffView.as_view()),
]
