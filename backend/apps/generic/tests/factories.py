from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from factory import LazyAttribute, LazyFunction, SelfAttribute, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from apps.generic.models import Reaction

faker = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]

    username = LazyFunction(lambda: faker.user_name())
    email = LazyFunction(lambda: faker.email())
    first_name = LazyFunction(lambda: faker.first_name())
    last_name = LazyFunction(lambda: faker.last_name())


class GroupFactory(DjangoModelFactory):
    name = LazyFunction(lambda: faker.name())

    class Meta:
        model = Group


class ReactionFactory(DjangoModelFactory):
    object_id = SelfAttribute("content_object.id")
    content_type = LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object)
    )
    reaction_type = LazyFunction(
        lambda: faker.random_choices(elements=Reaction.TYPE_CHOICES)
    )

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
