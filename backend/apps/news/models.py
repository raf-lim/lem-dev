from os.path import join

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django_extensions.db.fields import (
    AutoSlugField,
    CreationDateTimeField,
    ModificationDateTimeField,
)

# from apps.generic.models import Like


class UserActionTimestamp(models.Model):
    """Abstract model to inherit datetime for obcject creation and/or
    edit by user as well as inherit foreign key to User object."""

    class Meta:
        abstract = True
        ordering = ("-created_at",)

    created_at = CreationDateTimeField()
    modified_at = ModificationDateTimeField()
    # created = models.DateTimeField(auto_now_add=True)
    # edited = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # option
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class PolymorphicRelationship(models.Model):
    """Abstract model to inherit generic relationship (polymorphic)
    setup."""

    class Meta:
        abstract = True

    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")


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


class File(UserActionTimestamp, PolymorphicRelationship):
    MEDIA_TYPE = "files"

    file = models.FileField(upload_to=directory_path, blank=True, null=True)
    # TODO allow only one file?

    def __str__(self) -> str:
        return self.file.url


class Image(UserActionTimestamp, PolymorphicRelationship):
    MEDIA_TYPE = "images"

    image = models.ImageField(upload_to=directory_path, blank=True, null=True)
    alt_text = models.CharField(max_length=255)
    # TODO allow only one picture?

    def __str__(self) -> str:
        return self.image.url


class Tag(UserActionTimestamp, PolymorphicRelationship):
    class Meta:
        ordering = ["name"]

    name = models.CharField(unique=True, max_length=50)  # autocomplete?
    # TODO validate input for name?
    slug = AutoSlugField(populate_from="name")

    def __str__(self) -> str:
        return self.name


class Highlight(UserActionTimestamp, PolymorphicRelationship):
    highlight = models.BooleanField(default=True)

    def __str__(self):
        return str(self.highlight)


# TODO remove Like model when generic one ready to import.
class Like(UserActionTimestamp, PolymorphicRelationship):
    like = models.BooleanField(default=True)

    def __str__(self):
        return str(self.like)


class Comment(UserActionTimestamp, PolymorphicRelationship):
    body = models.TextField(null=False, blank=False)
    # TODO validate input for body?

    # TODO consider GenericRelation for related likes or other reactions
    # and activate when import available.
    # likes = GenericRelation(Like, related_query_name="comment")

    def __str__(self) -> str:
        return self.body[:20]


# TODO consider potential use of model manager
# class NewsManager(models.Manager):
#     # override default get_queryset and returns published news
#     def get_queryset(self) -> QuerySet:
#         return self.all_objects().filter(is_published=True)
#
#     # call this function for getting all news (default get_queryset)
#     def all_objects(self) -> QuerySet:
#         return super().get_queryset()
#
#     # call this function for getting not published news
#     def inactive(self) -> QuerySet:
#         return self.all_objects().filter(is_published=False)


class News(UserActionTimestamp):
    class Meta:
        verbose_name_plural = "News"

    title = models.CharField(null=False, blank=False, max_length=200)
    # TODO title validator?
    slug = AutoSlugField(populate_from="title")
    body = models.TextField(null=False, blank=False)
    # TODO validator, html safety issue?
    is_published = models.BooleanField(default=False)

    # TODO consider the use these fields:
    allow_highlights = models.BooleanField(null=False, blank=False, default=True)
    allow_likes = models.BooleanField(null=False, blank=False, default=True)
    allow_comments = models.BooleanField(null=False, blank=False, default=True)

    # TODO consider below generic ralations:
    files = GenericRelation(File, related_query_name="news")  # interview text
    images = GenericRelation(Image, related_query_name="news")  # news image
    tags = GenericRelation(Tag, related_query_name="news")
    highlights = GenericRelation(Highlight, related_query_name="news")
    likes = GenericRelation(Like, related_query_name="news")
    comments = GenericRelation(Comment, related_query_name="news")

    # TODO consider potential use of model manager
    # objects = NewsManager()

    def __str__(self) -> str:
        return self.title

    # TODO consider if comments shall be serialized with the news
    # Can be used to include comments to news response if needed.
    @property
    def comments_list(self):
        return self.comments.all()

    # TODO consider as above, distinct() can be applied.
    @property
    def tags_list(self):
        return self.tags.all()

    def get_absolute_url(self):
        return reverse("news-detail", args=[self.slug])
        # return reverse("news_detail", kwargs={"pk": self.pk, "slug": self.slug})
        # return f"{self.id}-{self.slug}"
