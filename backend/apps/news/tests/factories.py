from datetime import datetime

import factory
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from factory import fuzzy
from pytz import UTC

from apps.news.models import Tag
from apps.users.tests.factories import UserFactory


class NewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "news.News"

    user = factory.SubFactory(UserFactory)

    created = factory.LazyAttribute(
        lambda x: fuzzy.FuzzyDateTime(start_dt=datetime(2010, 1, 1, tzinfo=UTC))
    )
    modified = factory.LazyAttribute(
        lambda x: fuzzy.FuzzyDateTime(start_dt=datetime(2012, 1, 1, tzinfo=UTC))
    )
    title = factory.LazyAttribute(lambda x: fuzzy.FuzzyText().fuzz())
    slug = factory.LazyAttribute(lambda x: slugify(x.title))
    body = factory.LazyAttribute(lambda x: fuzzy.FuzzyText(length=200).fuzz())
    is_published = False
    allow_highlights = True
    allow_likes = True
    allow_comments = True


class PolymorficRelationshipFactory(factory.django.DjangoModelFactory):
    class Meta:
        exclude = "content_objects"
        abstract = True

    object_id = factory.SelfAttribute("content_object.id")
    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object)
    )


class TaggedNewsFactory(PolymorficRelationshipFactory):
    class Meta:
        model = Tag

    object_content = factory.SubFactory(NewsFactory)
