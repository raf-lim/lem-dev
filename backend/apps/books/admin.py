from django.contrib import admin

from .models import Author, Book, BookLanguage, BookPublisher, BookSize, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    search_fields = ("title",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(BookPublisher)
class BookPublisherAdmin(admin.ModelAdmin):
    list_display = ("id", "publisher")
    search_fields = ("publisher",)


@admin.register(BookLanguage)
class BookLanguageAdmin(admin.ModelAdmin):
    list_display = ("id", "language", "shortcut_language")
    search_fields = ("shortcut_language",)


@admin.register(BookSize)
class BookSizeAdmin(admin.ModelAdmin):
    list_display = ("id", "x_size", "y_size")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    search_fields = ("first_name",)
