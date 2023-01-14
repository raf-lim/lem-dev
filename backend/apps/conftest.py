import pytest

from apps.news.models import News
from apps.news.tests.factories import NewsFactory
from apps.users.models import User
from apps.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def user(db) -> User:
    return UserFactory()


@pytest.fixture()
def news() -> News:
    return NewsFactory()
