# Generated by Django 4.1.4 on 2023-01-15 18:51

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True, editable=False, populate_from="tag"
            ),
        ),
    ]
