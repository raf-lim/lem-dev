"""News app admin registered models."""

from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "slug", "is_published", "user"]
