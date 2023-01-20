from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import (
    AutoSlugField,
    CreationDateTimeField,
    ModificationDateTimeField,
)

# from django.urls import reverse
# from django.db.models import Avg
# from django.db.models.query import QuerySet


# TODO in progress
# temporary here, move to books/models if available?

# class AuthorManager(models.Manager):
#     """Queryset manager for Author model."""

#     # def get_queryset(self) -> QuerySet:
#     #     """Build-in queryset"""
#     #     return super().get_queryset()

#     def genres(self) -> QuerySet:
#         """Returns genres that author's books belong to."""
#         # TODO query to be checked, not sure it works this way
#         return self.books.genres.all().distinct()

#     def scoring(self) -> float:
#         """Returns average of author's books' scoring."""
#         # TODO query to be checked, not sure it works this way
#         return self.books.reviews.all().aggregate(Avg("score"))


class Author(models.Model):
    """Model for books' authors."""

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")
        ordering = ("first_name",)

    first_name = models.CharField(max_length=64, verbose_name=_("first name"))
    middle_name = models.CharField(
        max_length=64, null=True, blank=True, verbose_name=_("middle name")
    )
    last_name = models.CharField(max_length=64, verbose_name=_("last name"))
    full_name = models.CharField(max_length=255, verbose_name=_("full name"))
    slug = AutoSlugField(populate_from=["first_name", "last_name"])

    birth_date = models.DateField(
        null=True, blank=True, verbose_name=_("date of birth")
    )
    death_date = models.DateField(
        null=True, blank=True, verbose_name=_("date of death")
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

    # trial
    def make_full_name(self) -> str:
        """Author's full name."""
        if not self.mid_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.first_name} {self.mid_name} {self.last_name}"

    def get_absolute_url(self) -> str:
        # return reverse("authors-detail", args=[self.slug])
        pass

    # TODO check the save function.
    def save(self, *args, **kwargs):
        self.full_name = self.make_full_name()
        return super().save(*args, **kwargs)


class Genre(models.Model):
    """Genre database model"""

    GENRES = (
        ("LF", "Literary Fiction"),
        ("My", "Mystery"),
        ("Th", "Thriller"),
        ("Ho", "Horror"),
        ("Hi", "Historical"),
        ("Ro", "Romance"),
        ("We", "Western"),
        ("Bi", "Bildungsroman"),
        ("SpF", "Speculative Fiction"),
        ("SF", "Science Fiction"),
        ("Fa", "Fantasy"),
        ("Dy", "Dystopian"),
        ("MR", "Magical Realism"),
        ("RL", "Realist Literature"),
    )

    name = models.CharField(max_length=25, choices=GENRES)


class Book(models.Model):
    """Book database model"""

    TYPE_OF_COVER = (
        ("PB", "Paperback"),
        ("HC", "Hardcover Casewrap"),
        ("HDJ", "Hardcover Dust Jacket"),
    )
    PUBLICATION_FORMATS = (
        ("ebook", "E-Book format"),
        ("textbook", "Textbook format"),
    )

    title = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex="^[a-zA-Z0-9]*$",
                message="Title must be Alphanumeric",
                code="invalid_title",
            ),
        ],
    )
    original_title = models.CharField(
        max_length=255,
        blank=True,
        validators=[
            RegexValidator(
                regex="^[a-zA-Z0-9]*$",
                message="Title must be Alphanumeric",
                code="invalid_title",
            ),
        ],
    )
    year_of_publication = models.IntegerField()
    publisher = models.ForeignKey("BookPublisher", on_delete=models.CASCADE)
    issue_number = models.IntegerField(default=1)
    number_of_page = models.IntegerField()
    type_of_cover = models.CharField(max_length=55, choices=TYPE_OF_COVER)
    describe = models.TextField()
    publication_formats = models.CharField(max_length=55, choices=PUBLICATION_FORMATS)
    language_provided = models.ForeignKey("BookLanguage", on_delete=models.CASCADE)
    original_language = models.CharField(max_length=55)
    dimensions = models.ForeignKey("BookSize", on_delete=models.CASCADE)
    catalog_number = models.IntegerField()
    ISBN_id = models.IntegerField()
    genre = models.ManyToManyField(Genre, related_name="books")

    # author field
    author = models.ManyToManyField(Author, related_name="books")


class BookLanguage(models.Model):
    """Language of book database model"""

    language = models.CharField(max_length=50)
    shortcut_language = models.CharField(max_length=10)


class BookPublisher(models.Model):
    """Publisher for books database model"""

    publisher = models.CharField(max_length=50)


class BookSize(models.Model):
    """Dimension of books database model"""

    x_size = models.IntegerField(default=0)
    y_size = models.IntegerField(default=0)


class Review(models.Model):
    """Review database model"""

    # author field
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
