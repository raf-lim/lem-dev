# Generated by Django 4.1.4 on 2022-12-30 01:00

import django.core.validators
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                editable=False,
                populate_from=["slug_datetime", "title"],
                verbose_name="Post slug",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(
                max_length=100,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Input must contain only alphabetic characters (' and \" included) and spaces",
                        regex="^[a-zA-Z\\'\\\" ]+$",
                    )
                ],
                verbose_name="Post title",
            ),
        ),
    ]