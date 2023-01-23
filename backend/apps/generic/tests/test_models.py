import pytest

from apps.generic.models import Reaction
from apps.generic.tests.factories import ReactionUserFactory


@pytest.mark.django_db()
class TestReactionModel:
    def test_fields(self):
        assert get_field(Reaction, "user")
        assert get_field(Reaction, "object_id")
        assert get_field(Reaction, "content_type")
        assert get_field(Reaction, "reaction_type")
        # assert get_field(Reaction, "content_object")

    @pytest.fixture()
    def user_factory(self):
        return ReactionUserFactory()

    def test_reaction_type(self, user_factory):
        assert user_factory.content_object == "test"


def get_field(model, field):
    return getattr(model, field).field
