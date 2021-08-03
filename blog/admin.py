from django.contrib import admin

# Register your models here.
from blog.models import Blog, Ctegory, Comment

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Ctegory)
