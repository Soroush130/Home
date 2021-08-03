from django.urls import path, include

from contact.views import contact_page

urlpatterns = [
    path('contact', contact_page)
]
