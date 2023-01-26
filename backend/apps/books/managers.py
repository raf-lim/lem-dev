from django.db import models
from django.db.models import Avg

# from django.db.models.query import QuerySet

# from django.urls import reverse


class ReviewManager(models.Manager):
    def positive_reviews(self):
        return self.filter(score__gte=3)

    def negative_reviews(self):
        return self.filter(score__lt=3)


class BookQuerySet(models.QuerySet):
    def get_author_books(self, author_id):
        return self.filter(author__id=author_id)


class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, using=self._db)

    def get_author_books(self, author_id):
        return self.get_queryset().get_author_books(author_id)

    def get_scoring_average(self, author_id):
        pass


class AuthorQuerySet(models.QuerySet):
    def get_scoring_average(self) -> float:
        """Returns average of author's books' scoring."""
        return self.books.reviews.all().aggregate(Avg("score"))

    def get_absolute_url(self):
        # return reverse("authors-detail", args=[self.slug])
        pass

    def get_update_url(self):
        # return reverse("authors-update", args=[self.slug])
        pass

    def get_delete_url(self):
        # return reverse("authors-delete", args=[self.slug])
        pass

    def get_full_name(self) -> str:
        """Author's full name."""
        if not self.middle_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    # def get_absolute_url(self) -> str:
    #     # return reverse("authors-detail", args=[self.slug])
    #     pass


class AuthorManager(models.Manager):
    """Model manager for Author's model."""

    def get_queryset(self):
        return AuthorQuerySet(self.model, using=self._db)

    def get_books(self):
        return self.get_queryset().get_books()

    def get_genres(self):
        return self.get_queryset().get_genres()

    def get_scoring_average(self):
        return self.get_queryset().get_scoring_average()

    def get_full_name(self):
        return self.get_queryset().get_full_name()
