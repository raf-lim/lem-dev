"""Generic app serializers."""

from rest_framework import serializers

from .models import Comment, Highlight, Reaction, Review, Tag

# class FileSerializer(serializers.ModelSerializer):
#     """Serializer for File model."""

#     class Meta:
#         model = File
#         fields = "__all__"

#     # serializing File object id (required for listing from property)
#     id = serializers.IntegerField(required=False)


class HighlightSerializer(serializers.ModelSerializer):
    """Serializer for Hightlight model"""

    class Meta:
        model = Highlight
        fields = "__all__"
        read_only_fields = ("news",)

    id = serializers.IntegerField(required=False)


class ReactionSerializer(serializers.ModelSerializer):
    """Serializer for Review model."""

    class Meta:
        model = Reaction
        fields = "__all__"
        read_only_fields = ("book", "comment")

    # serializing Review object id (required for listing from property)
    id = serializers.IntegerField(required=False)


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model."""

    class Meta:
        model = Tag
        fields = "__all__"
        read_only_fields = ("books", "news")

    # serializing Tag object id (required for listing from property)
    id = serializers.IntegerField(required=False)


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("news",)

    # serializing Comment object id (required for listing from property)
    id = serializers.IntegerField(required=False)


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model."""

    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ("book",)

    # serializing Review object id (required for listing from property)
    id = serializers.IntegerField(required=False)
