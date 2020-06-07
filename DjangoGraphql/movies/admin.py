from django.contrib import admin
from .models import Category
from .models import Movie


admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)