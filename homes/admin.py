from django.contrib import admin

# Register your models here.
from homes.models import Home, HomeType, Amenities, HomeGallery, City, Message, Variant

admin.site.register(Home)
admin.site.register(HomeType)
admin.site.register(Amenities)
admin.site.register(HomeGallery)
admin.site.register(City)
admin.site.register(Message)
admin.site.register(Variant)