from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from factory import LazyAttribute, SelfAttribute, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from apps.generic.models import Reaction


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]

    username = Faker("user_name")
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")


class GroupFactory(DjangoModelFactory):
    name = "group"

    class Meta:
        model = Group


class ReactionFactory(DjangoModelFactory):
    object_id = SelfAttribute("content_object.id")
    content_type = LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object)
    )
    reaction_type = Faker("random_choices", elements=Reaction.TYPE_CHOICES)

    class Meta:
        exclude = ["content_object"]
        abstract = True


class ReactionUserFactory(ReactionFactory):
    content_object = SubFactory(UserFactory)

    class Meta:
        model = Reaction


class ReactionGroupFactory(ReactionFactory):
    content_object = SubFactory(GroupFactory)

    class Meta:
        model = Reaction
