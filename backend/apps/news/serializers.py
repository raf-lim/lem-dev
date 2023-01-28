"""News app serializers."""

from apps.generic.models import Comment, Highlight, Tag
from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    """Serializer for News model."""

    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = ("news",)
        # to use slug instead of id in the url:
        # extra_kwargs = {"url": {"lookup_field": "slug"}}

    url = serializers.CharField(source="get_absolute_url", read_only=True)

    """Serializing property filed in News model.
    Property comments_list can be used to include comments to news responce
    and in such case it must be included in fields list in Meta class."""
    # comments_list = CommentSerializer(many=True, required=False)
    # tags_list = TagSerializer(many=True, required=False)
