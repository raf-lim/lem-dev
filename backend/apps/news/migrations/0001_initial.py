# Generated by Django 4.1.4 on 2023-01-14 18:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                (
                    "tag",
                    models.CharField(
                        help_text="Must be unique, only alphanumeric allowed",
                        max_length=50,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                3, message="Min length is 3 characters."
                            ),
                            django.core.validators.MaxLengthValidator(
                                50, message="Max length is 200 characters."
                            ),
                            django.core.validators.RegexValidator(
                                re.compile("^[-a-zA-Z0-9_]+\\Z"),
                                "Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.",
                                "invalid",
                            ),
                        ],
                    ),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True, editable=False, populate_from="name"
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "ordering": ["tag"],
            },
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Min lenght of 3 chars, max length of 200 chars, only alphanumeric, ', \", dot and space allowed",
                        max_length=200,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                3, message="Min length is 3 characters."
                            ),
                            django.core.validators.MaxLengthValidator(
                                200, message="Max length is 200 characters."
                            ),
                            django.core.validators.RegexValidator(
                                message="Only alphanumeric, ', \", dot and space allowed.",
                                regex="^[\\w\\.\\'\\\" ]+$",
                            ),
                        ],
                        verbose_name="news title",
                    ),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True, editable=False, populate_from=["title"]
                    ),
                ),
                ("body", models.TextField(verbose_name="news body")),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="is published"),
                ),
                (
                    "allow_highlights",
                    models.BooleanField(default=True, verbose_name="allow highlights"),
                ),
                (
                    "allow_likes",
                    models.BooleanField(default=True, verbose_name="allow likes"),
                ),
                (
                    "allow_comments",
                    models.BooleanField(default=True, verbose_name="allow comments"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "news",
            },
        ),
        migrations.CreateModel(
            name="Highlight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                ("highlight", models.BooleanField(default=False)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "highlight",
                "verbose_name_plural": "highlights",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                ("body", models.TextField()),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
                "abstract": False,
            },
        ),
    ]
