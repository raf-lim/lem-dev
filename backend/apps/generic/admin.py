"""Generic app admin registered models."""

from django.contrib import admin

from .models import Comment, Highlight, Reaction, Review, Tag


@admin.register(Highlight)
class Highlightdmin(admin.ModelAdmin):
    list_display = ["pk", "highlight", "content_object", "user"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["pk", "tag", "slug", "content_object", "user"]
    search_fields = ["name"]
    # prepopulated_fields = {"slug": ("name",)}


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ["pk", "reaction_type", "content_object", "user"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["pk", "content", "content_object", "user"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["pk", "content", "content_object", "user"]


# @admin.register(File)
# class FileAdmin(admin.ModelAdmin):
#     list_display = ["pk", "file", "content_object", "user"]


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ["pk", "image", "alt_text", "content_object", "user"]
