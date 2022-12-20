from django.db import models


class Book(models.Model):
    """Book database model"""

    TYPE_OF_COVER = (
        ("PB", "Paperback"),
        ("HC", "Hardcover Casewrap"),
        ("HDJ", "Hardcover Dust Jacket"),
    )
    PUBLICATION_FORMATS = (
        ("ebook", "E-Book format"),
        ("textbook", "Textbook format"),
    )

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    author = models.CharField(max_length=55)
    year_of_publication = models.IntegerField()
    publisher = models.CharField(max_length=55)
    issue_number = models.IntegerField(default=1)
    number_of_page = models.IntegerField()
    type_of_cover = models.CharField(max_length=55, choices=TYPE_OF_COVER)
    describe = models.CharField(max_length=255)
    publication_formats = models.CharField(max_length=55, choices=PUBLICATION_FORMATS)
    language_provided = models.CharField(max_length=55)
    original_language = models.CharField(max_length=55)
    dimensions = models.CharField(max_length=255)
    catalog_number = models.IntegerField()
    ISBN_id = models.IntegerField()
    review = models.ForeignKey("Review", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)


class Genre(models.Model):
    """Genre database model"""

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)


class Review(models.Model):
    """Review database model"""

    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
