# Generated by Django 4.1.4 on 2023-01-13 22:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                    "title",
                    models.CharField(
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_title",
                                message="Title must be Alphanumeric",
                                regex="^[a-zA-Z0-9]*$",
                            )
                        ],
                    ),
                ),
                (
                    "original_title",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_title",
                                message="Title must be Alphanumeric",
                                regex="^[a-zA-Z0-9]*$",
                            )
                        ],
                    ),
                ),
                ("year_of_publication", models.IntegerField()),
                ("issue_number", models.IntegerField(default=1)),
                ("number_of_page", models.IntegerField()),
                (
                    "type_of_cover",
                    models.CharField(
                        choices=[
                            ("PB", "Paperback"),
                            ("HC", "Hardcover Casewrap"),
                            ("HDJ", "Hardcover Dust Jacket"),
                        ],
                        max_length=55,
                    ),
                ),
                ("describe", models.TextField()),
                (
                    "publication_formats",
                    models.CharField(
                        choices=[
                            ("ebook", "E-Book format"),
                            ("textbook", "Textbook format"),
                        ],
                        max_length=55,
                    ),
                ),
                ("original_language", models.CharField(max_length=55)),
                ("catalog_number", models.IntegerField()),
                ("ISBN_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="BookLanguage",
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
                ("language", models.CharField(max_length=50)),
                ("shortcut_language", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="BookPublisher",
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
                ("publisher", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="BookSize",
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
                ("x_size", models.IntegerField(default=0)),
                ("y_size", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
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
                    "name",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=25,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                ("content", models.CharField(max_length=255)),
                ("score", models.IntegerField(default=0)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="books.book"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="dimensions",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="books.booksize"
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="genre",
            field=models.ManyToManyField(to="books.genre"),
        ),
        migrations.AddField(
            model_name="book",
            name="language_provided",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="books.booklanguage"
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="publisher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="books.bookpublisher"
            ),
        ),
    ]
