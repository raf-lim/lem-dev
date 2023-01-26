from django.contrib import admin

from .models import Author, Book, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    search_fields = ("title",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    search_fields = ("first_name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
