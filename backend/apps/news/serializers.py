"""News app serializers."""

from rest_framework import serializers

from .models import Comment, File, News, Tag


class FileSerializer(serializers.ModelSerializer):
    """Serializer for File model."""

    class Meta:
        model = File
        fields = "__all__"

    # serializing File object id (required for listing from property)
    id = serializers.IntegerField(required=False)


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("news",)

    # serializing Comment object id (required for listing from property)
    id = serializers.IntegerField(required=False)


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model."""

    class Meta:
        model = Tag
        fields = "__all__"
        read_only_fields = ("news",)

    # serializing Tag object id (required for listing from property)
    id = serializers.IntegerField(required=False)


class NewsSerializer(serializers.ModelSerializer):
    """Serializer for News model."""

    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = ("news",)

    """Serializing property filed in News model.
    Property comments_list can be used to include comments to news responce
    and in such case it must be included in fields list in Meta class."""
    # comments_list = CommentSerializer(many=True, required=False)
    # tags_list = TagSerializer(many=True, required=False)
