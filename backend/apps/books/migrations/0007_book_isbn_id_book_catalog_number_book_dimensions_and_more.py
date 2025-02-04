# Generated by Django 4.1.4 on 2023-01-27 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0006_alter_book_options_author_user_book_created_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="ISBN_id",
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="catalog_number",
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="dimensions",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="books.booksize",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="language_provided",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="books.booklanguage",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="original_language",
            field=models.CharField(default="polish", max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="book",
            name="publisher",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="books.bookpublisher",
            ),
            preserve_default=False,
        ),
    ]
