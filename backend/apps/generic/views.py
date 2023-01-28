"""Generic app views"""

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Comment, Highlight, Reaction, Review, Tag
from .serializers import (
    CommentSerializer,
    HighlightSerializer,
    ReactionSerializer,
    ReviewSerializer,
    TagSerializer,
)

# class FileViewSet(viewsets.ModelViewSet):
#     queryset = File.objects.all()
#     serializer_class = FileSerializer
#     # TODO remove, temporary
#     permission_classes = [AllowAny]


class HighlightViewSet(viewsets.ModelViewSet):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer
    # TODO remove, temporary
    permission_classes = [AllowAny]


class ReactionViewSet(viewsets.ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    # TODO remove, temporary
    permission_classes = [AllowAny]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # TODO remove, temporary
    permission_classes = [AllowAny]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # TODO remove, temporary
    permission_classes = [AllowAny]
    lookup_field = "pk"


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # TODO remove, temporary
    permission_classes = [AllowAny]
    lookup_field = "pk"
