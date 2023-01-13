"""News app models"""
from os.path import join
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
    validate_slug,
)
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import (
    AutoSlugField,
    CreationDateTimeField,
    ModificationDateTimeField,
)

# from apps.generic.models import Like, File, Picture


class UserActionTimestampedMixin(models.Model):
    """Abstract model to inherit timestamp for obcject creation or
    modification by user as well as inherit foreign key to User object."""

    class Meta:
        abstract = True
        ordering = ("-created",)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user")
    )


class PolymorphicRelationship(models.Model):
    """Abstract model to inherit generic relationship (polymorphic)
    setup."""

    class Meta:
        abstract = True

    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")


class Highlight(UserActionTimestampedMixin, PolymorphicRelationship):
    """Highlight model"""

    class Meta:
        verbose_name = _("highlight")
        verbose_name_plural = _("highlights")

    highlight = models.BooleanField(default=False)

    def __str__(self):
        return str(self.highlight)


class Tag(UserActionTimestampedMixin, PolymorphicRelationship):
    """Tag model"""

    class Meta:
        ordering = ["name"]

    name = models.CharField(
        unique=True,
        max_length=50,
        validators=[
            MinLengthValidator(3, message=_("Min length is 3 characters.")),
            MaxLengthValidator(50, message=_("Max length is 200 characters.")),
            validate_slug,
        ],
        help_text=_("Must be unique, only alphanumeric allowed"),
    )
    slug = AutoSlugField(populate_from="name")

    def __str__(self) -> str:
        return self.name


class Comment(UserActionTimestampedMixin, PolymorphicRelationship):
    """Comment model"""

    body = models.TextField(null=False, blank=False)
    # TODO add validators

    # likes = GenericRelation(Like, related_query_name="comment")

    def __str__(self) -> str:
        return self.body[:20]


def directory_path(instance, filename: str) -> str:
    """Returns file path including app name, media type, content type name,
    and file object id.

    Args:
        instance (class instance): File or Image class object
        filename (str): filename

    Returns:
        str: image's or file's path string
    """
    dir_path = join(
        instance.content_type.app_label,
        instance.MEDIA_TYPE,
        f"{instance.content_type.name}-{instance.object_id}",
    )
    return join(dir_path, filename)


class File(UserActionTimestampedMixin, PolymorphicRelationship):
    MEDIA_TYPE = "files"

    file = models.FileField(upload_to=directory_path, blank=True, null=True)
    # TODO allow only one file?

    def __str__(self) -> str:
        return self.file.url


class Image(UserActionTimestampedMixin, PolymorphicRelationship):
    MEDIA_TYPE = "images"

    image = models.ImageField(upload_to=directory_path, blank=True, null=True)
    alt_text = models.CharField(max_length=255)
    # TODO allow only one picture?

    def __str__(self) -> str:
        return self.image.url


# TODO remove Like model when generic one ready to import.
class Like(UserActionTimestampedMixin, PolymorphicRelationship):
    like = models.BooleanField(default=True)

    def __str__(self):
        return str(self.like)


# draft for further development depending on needs
class NewsManager(models.Manager):
    """Manager for News"""

    def get_queryset(self):
        """Returns queryset with published news objects."""
        return self.all_objects().filter(is_published=True)

    def all_objects(self):
        """Returns queryest with all news objects (default get_queryset)"""
        return super().get_queryset()

    def inactive(self):
        """Returns queryset with not published news objects"""
        return self.all_objects().filter(is_published=False)


class News(UserActionTimestampedMixin):
    """News model"""

    class Meta:
        verbose_name_plural = _("news")

    title = models.CharField(
        null=False,
        blank=False,
        max_length=200,
        validators=[
            MinLengthValidator(3, message=_("Min length is 3 characters.")),
            MaxLengthValidator(200, message=_("Max length is 200 characters.")),
            RegexValidator(
                regex=r"^[\w\.\'\" ]+$",
                message=_("Only alphanumeric, ', \", dot and space allowed."),
            ),
        ],
        help_text=_(
            "Min lenght of 3 chars, max length of 200 chars, only alphanumeric, ', \", dot and space allowed"
        ),
        verbose_name=_("news title"),
    )
    slug = AutoSlugField(populate_from=["title"])

    body = models.TextField(null=False, blank=False, verbose_name=_("news body"))
    # TODO add body validator, html safety issue?

    is_published = models.BooleanField(default=False, verbose_name=_("is published"))
    allow_highlights = models.BooleanField(
        null=False, blank=False, default=True, verbose_name=_("allow highlights")
    )
    allow_likes = models.BooleanField(
        null=False, blank=False, default=True, verbose_name=_("allow likes")
    )
    allow_comments = models.BooleanField(
        null=False, blank=False, default=True, verbose_name=_("allow comments")
    )

    # objects = NewsManager()

    # files = GenericRelation(File, related_query_name="news")  # interview text
    # images = GenericRelation(Image, related_query_name="news")  # news image

    tags = GenericRelation(Tag, related_query_name="news")
    highlights = GenericRelation(Highlight, related_query_name="news")

    # likes = GenericRelation(Like, related_query_name="news")

    comments = GenericRelation(Comment, related_query_name="news")

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("news-detail", args=[self.slug])
