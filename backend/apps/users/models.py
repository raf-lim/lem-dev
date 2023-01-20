from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Avg
from django.db.models.query import QuerySet

# from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import (
    AutoSlugField,
    CreationDateTimeField,
    ModificationDateTimeField,
)


class User(AbstractUser):
    pass


# TODO in progress
# temporary here, move to books/models if available?


class AuthorManager(models.Manager):
    """Queryset manager for Author model."""

    # def get_queryset(self) -> QuerySet:
    #     """Build-in queryset"""
    #     return super().get_queryset()

    def genres(self) -> QuerySet:
        """Returns genres that author's books belong to."""
        # TODO query to be checked, not sure it works this way
        return self.books.genres.all().distinct()

    def scoring(self) -> float:
        """Returns average of author's books' scoring."""
        # TODO query to be checked, not sure it works this way
        return self.books.reviews.all().aggregate(Avg("score"))


class Author(models.Model):
    """Model for books' authors."""

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")
        ordering = ("first_name",)

    first_name = models.CharField(max_length=150, verbose_name=_("first_name"))
    middle_name = models.CharField(
        max_length=150, null=True, blank=True, verbose_name=_("middle_name")
    )
    last_name = models.CharField(max_length=150, verbose_name=_("last_name"))
    slug = AutoSlugField(populate_from=["first_name", "last_name"])

    birth_date = models.DateField(
        null=True, blank=True, verbose_name=_("date_of_birth")
    )
    death_date = models.DateField(
        null=True, blank=True, verbose_name=_("date_of_death")
    )

    description = models.TextField(null=True, blank=True, verbose_name=_("description"))

    allow_highlights = models.BooleanField(
        null=False, blank=False, default=True, verbose_name=_("allow highlights")
    )

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    # objects = AuthorManager()

    # from apps.generic.modles import Highlight, Image
    # images = GenericRelation(Image, related_query_name="authors")
    # highlights = GenericRelation(Highlight, related_query_name="authors")

    def __str__(self) -> str:
        return self.full_name

    @property
    def full_name(self) -> str:
        """Author's full name."""
        if not self.mid_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.first_name} {self.mid_name} {self.last_name}"

    def get_absolute_url(self) -> str:
        # return reverse("authors-detail", args=[self.slug])
        pass


class Book(models.Model):
    authors = models.ManyToManyField(Author, related_name="books")


class Review(models.Model):
    """Review database model"""

    # TODO add related_name to book foreing key field
    content = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
