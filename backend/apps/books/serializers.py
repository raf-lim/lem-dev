"""Books app serializers."""

from apps.generic.models import Review
from rest_framework import serializers

from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book model."""

    class Meta:
        model = Book
        fields = "__all__"
        # to use slug instead of id in the url:
        # extra_kwargs = {"url": {"lookup_field": "slug"}}

    url = serializers.CharField(source="get_absolute_url", read_only=True)


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author model."""

    class Meta:
        model = Author
        fields = "__all__"
        # to use slug instead of id in the url:
        # extra_kwargs = {"url": {"lookup_field": "slug"}}

    url = serializers.CharField(source="get_absolute_url", read_only=True)
