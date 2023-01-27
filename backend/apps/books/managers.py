from django.db import models
from django.db.models import Avg

# from django.db.models.query import QuerySet

# from django.urls import reverse


class ReviewManager(models.Manager):
    def positive_reviews(self):
        return self.filter(score__gte=3)

    def negative_reviews(self):
        return self.filter(score__lt=3)


class AuthorQuerySet(models.QuerySet):
    def get_books(self, author_id):
        return self.filter(books__author__id=author_id)

    def get_absolute_url(self):
        # return reverse("authors-detail", args=[self.slug])
        pass


class AuthorManager(models.Manager):
    """Model manager for Author's model."""

    def get_queryset(self):
        return AuthorQuerySet(self.model, using=self._db)

    def get_books(self, author_id):
        return self.get_queryset().get_books(author_id)

    def get_scoring_average(self, author_id):
        return self.get_books(author_id)
