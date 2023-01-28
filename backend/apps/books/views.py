"""Book app views"""

from apps.generic.models import Review
from apps.generic.serializers import ReviewSerializer
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # to use slug instead of id in the url:
    # lookup_field = "slug"

    # TODO remove, temporary
    permission_classes = [AllowAny]

    @action(detail=True, methods=["GET"])
    def reviews(self, request, pk=None):
        """List reviews related to the book."""
        reviews = Review.objects.filter(book__id=pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response({"reviews": serializer.data}, status=200)

    @action(detail=True, methods=["GET"])
    def authors(self, request, pk=None):
        """List authors related to the book."""
        book_authors = Author.objects.filter(books__id=pk)
        serializer = AuthorSerializer(book_authors, many=True)
        return Response({"authors": serializer.data}, status=200)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # to use slug instead of id in the url:
    # lookup_field = "slug"

    # TODO remove, temporary
    permission_classes = [AllowAny]

    @action(detail=True, methods=["GET"])
    def books(self, request, pk=None):
        """List reviews related to the book."""
        author_books = Book.objects.filter(authors__id=pk)
        serializer = BookSerializer(author_books, many=True)
        return Response({"reviews": serializer.data}, status=200)


# Temporary view to display welcome page.
def welcome(request):
    return HttpResponse("<h3>Welcome to books page</h3>")
