from django.contrib import admin

from apps.generic.models import Reaction


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    readonly_fields = ("content_object",)
