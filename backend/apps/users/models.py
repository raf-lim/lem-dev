from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import (
    AutoSlugField,
    CreationDateTimeField,
    ModificationDateTimeField,
)


class User(AbstractUser):
    pass


# temporary here, move to books/models if available?
class Author(models.Model):
    """Model for books' authors."""

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    first_name = models.CharField(max_length=150, verbose_name=_("first_name"))
    last_name = models.CharField(max_length=150, verbose_name=_("last_name"))

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    def __str__(self) -> str:
        return self.full_name
