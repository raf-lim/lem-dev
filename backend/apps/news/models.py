"""News app models"""

from apps.generic.models import (
    Comment,
    Highlight,
    Reaction,
    Tag,
    UserActionTimestampedMixin,
)
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
    validate_slug,
)
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField


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

    content = models.TextField(null=False, blank=False, verbose_name=_("news body"))
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
    likes = GenericRelation(Reaction, related_query_name="news")
    comments = GenericRelation(Comment, related_query_name="news")

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("news-detail", args=[self.slug])
