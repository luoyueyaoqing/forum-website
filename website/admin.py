from django.contrib import admin
from .models import User, Plate, Article, Comment


admin.site.register(User)
admin.site.register(Plate)
admin.site.register(Article)
admin.site.register(Comment)
