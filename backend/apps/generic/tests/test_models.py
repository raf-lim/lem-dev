import pytest
from django.contrib.contenttypes.models import ContentType

from apps.generic.models import Reaction
from apps.generic.tests.factories import ReactionGroupFactory, ReactionUserFactory


@pytest.mark.django_db()
class TestReactionModel:
    def test_fields(self):
        """
        Test the fields of the Reaction.
        """
        assert get_field(Reaction, "user")
        assert get_field(Reaction, "object_id")
        assert get_field(Reaction, "content_type")
        assert get_field(Reaction, "reaction_type")

    @pytest.fixture()
    def user_reaction_factory(self):
        """
        Create a batch of 10 user reactions with like reaction type.
        """
        return ReactionUserFactory.create_batch(10, reaction_type="L")

    def test_count_like_reaction(self, user_reaction_factory):
        """
        Test the count of like reactions.
        """
        like_reaction = Reaction.objects.filter(reaction_type="L")
        assert like_reaction.count() == 10

    def test_count_dislike_reaction(self, user_reaction_factory):
        """
        Test the count of dislike reactions.
        """
        dislike_reaction = Reaction.objects.filter(reaction_type="D")
        assert dislike_reaction.count() == 0

    def test_str(self, user_reaction_factory):
        """
        Test string representation of the reaction is correct.
        """
        reactions = Reaction.objects.all()[:2]
        assert str(reactions[0]) == str(user_reaction_factory[0])
        assert str(reactions[1]) == str(user_reaction_factory[1])

    def test_user_content_type(self, user_reaction_factory):
        """
        Test the content type of the reactions.
        """
        user_type = ContentType.objects.get(app_label="users", model="user")
        assert user_reaction_factory[0].content_type == user_type

    @pytest.fixture()
    def group_reaction_factory(self):
        """
        Create a group reaction factory.
        """
        return ReactionGroupFactory()

    def test_group_content_type(self, group_reaction_factory):
        """
        Test that the content type of the group reactions is 'auth.Group'
        """
        user_type = ContentType.objects.get(app_label="auth", model="group")
        assert group_reaction_factory.content_type == user_type


def get_field(model, field):
    return getattr(model, field).field
