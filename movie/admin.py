from django.contrib import admin

# Register your models here.
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'release_date', 'rating')
    ordering = ('release_date', 'movie_title',)
    search_fields = ('movie_title', 'rating', 'cast',)


# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'gender')
#    ordering = ('first_name', 'last_name',)
#    search_fields = ('first_name', 'last_name',)
