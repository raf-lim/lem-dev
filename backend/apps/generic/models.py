from apps.generic.managers import ReactionManager
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxLengthValidator, MinLengthValidator, validate_slug
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import (
    AutoSlugField,
    CreationDateTimeField,
    ModificationDateTimeField,
)

from .managers import ReactionManager


class UserActionTimestampedMixin(models.Model):
    """Abstract model to inherit timestamp for obcject creation or
    modification by user as well as to inherit foreign key to User object."""

    class Meta:
        abstract = True
        ordering = ("-created",)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_("user"),
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


class Reaction(UserActionTimestampedMixin, PolymorphicRelationship):
    """
    Model representing a reaction by a user on a piece of content.

    Fields:
        user (models.ForeignKey): Foreign key to the User who made the like.
        content_type (models.ForeignKey): Foreign key to the ContentType of the liked content.
        object_id (models.PositiveIntegerField): Primary key of the liked content.
        content_object (GenericForeignKey): Generic foreign key to the liked content.
    """

    class Meta:
        ordering = ["user"]
        verbose_name = "Reaction"
        verbose_name_plural = "Reactions"

    LIKE = "L"
    DISLIKE = "D"
    TYPE_CHOICES = [
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    ]
    reaction_type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    objects = ReactionManager()

    def __str__(self):
        return f"{self.reaction_type} {self.content_object}"


class Tag(UserActionTimestampedMixin, PolymorphicRelationship):
    """Tag model"""

    class Meta:
        ordering = ["tag"]

    tag = models.CharField(
        unique=True,
        max_length=50,
        validators=[
            MinLengthValidator(3, message=_("Min length is 3 characters.")),
            MaxLengthValidator(50, message=_("Max length is 200 characters.")),
            validate_slug,
        ],
        help_text=_("Must be unique, only alphanumeric allowed"),
    )
    slug = AutoSlugField(populate_from="tag")

    def __str__(self) -> str:
        return self.tag


class Comment(UserActionTimestampedMixin, PolymorphicRelationship):
    """Comment model"""

    content = models.TextField(null=False, blank=False)
    reaction = GenericRelation(Reaction, related_query_name="comment")

    def __str__(self) -> str:
        return self.content[:20]


class Review(UserActionTimestampedMixin, PolymorphicRelationship):
    """Review database model"""

    content = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    reaction = GenericRelation(Reaction, related_query_name="review")

    def __str__(self) -> str:
        return self.content[:20]
