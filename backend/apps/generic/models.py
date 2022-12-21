from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Like(models.Model):
    """
    Model representing a "like" by a user on a piece of content.

    Fields:
        user (models.ForeignKey): Foreign key to the User who made the like.
        content_type (models.ForeignKey): Foreign key to the ContentType of the liked content.
        object_id (models.PositiveIntegerField): Primary key of the liked content.
        content_object (GenericForeignKey): Generic foreign key to the liked content.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        """
        Meta options for the Like model.
        """

        ordering = ["user"]
        verbose_name = "Like"
        verbose_name_plural = "Likes"
