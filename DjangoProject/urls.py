from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from DjangoProject.views import about_page, header, footer, home_page, search_header

urlpatterns = [
    path('header', header, name="header"),
    path('footer', footer, name="footer"),
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about-us', about_page),
    path('list', search_header),
    path('', include("homes.urls")),
    path('', include("stuff.urls")),
    path('', include("blog.urls")),
    path('', include("contact.urls")),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
