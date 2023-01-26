"""News app admin registered models."""

from django.contrib import admin

from .models import Comment, Highlight, News, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["pk", "tag", "slug", "content_object", "user"]
    search_fields = ["name"]
    # prepopulated_fields = {"slug": ("name",)}


# @admin.register(File)
# class FileAdmin(admin.ModelAdmin):
#     list_display = ["pk", "file", "content_object", "user"]


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ["pk", "image", "alt_text", "content_object", "user"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["pk", "body", "content_object", "user"]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "slug", "is_published", "user"]


# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     list_display = ["pk", "like", "content_object", "user"]


@admin.register(Highlight)
class Highlightdmin(admin.ModelAdmin):
    list_display = ["pk", "highlight", "content_object", "user"]
