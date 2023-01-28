"""News app views"""

from apps.generic.serializers import (
    CommentSerializer,
    HighlightSerializer,
    TagSerializer,
)
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Comment, Highlight, News, Tag
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # to use slug instead of id in the url:
    lookup_field = "slug"

    # TODO remove, temporary
    permission_classes = [AllowAny]

    @action(detail=True, methods=["GET"])
    def comments(self, request, slug=None):
        """List comments related to the news."""
        comments = Comment.objects.filter(news__slug=slug)
        serializer = CommentSerializer(comments, many=True)
        return Response({"comments": serializer.data}, status=200)

    @action(detail=True, methods=["POST"])
    def comment(self, request, pk=None):
        """Create comment to news instance."""
        # news = self.get_object()
        # request.POST._mutable = True
        data = request.data
        data["object_id"] = pk
        data["content_type"] = ContentType.objects.get_for_id(id=pk).id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            # serializer.save(user=self.request.user)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=["GET"])
    def tags(self, request, pk=None):
        tags = Tag.objects.filter(news__id=pk)
        serializer = TagSerializer(tags, many=True)
        return Response({"tags": serializer.data}, status=200)

    @action(detail=True, methods=["POST"])
    def tag(self, request, pk=None):
        """Create tag to news instance."""
        # news = self.get_object()
        # request.POST._mutable = True
        data = request.data
        data["object_id"] = pk
        data["content_type"] = ContentType.objects.get_for_id(id=pk).id
        serializer = TagSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Temporary view to display welcome page.
def welcome(request):
    return HttpResponse("<h3>Welcome to news cms</h3>")
