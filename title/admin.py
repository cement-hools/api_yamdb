from django.contrib import admin

from title.models import Title, Category, Genre

admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Genre)