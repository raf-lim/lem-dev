from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.generic.managers import ReactionManager


class Reaction(models.Model):
    """
    Model representing a reaction by a user on a piece of content.

    Fields:
        user (models.ForeignKey): Foreign key to the User who made the like.
        content_type (models.ForeignKey): Foreign key to the ContentType of the liked content.
        object_id (models.PositiveIntegerField): Primary key of the liked content.
        content_object (GenericForeignKey): Generic foreign key to the liked content.
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")

    LIKE = "L"
    DISLIKE = "D"
    TYPE_CHOICES = [
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    ]
    reaction_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    objects = ReactionManager()

    class Meta:
        """
        Meta options for the Like model.
        """

        ordering = ["user"]
        verbose_name = "Reaction"
        verbose_name_plural = "Reactions"

    def __str__(self):
        return f"{self.reaction_type} {self.content_object}"
