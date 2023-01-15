import pytest
from pytest_factoryboy import register

from apps.news.tests.factories import NewsFactory
from apps.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


register(UserFactory)  # registers fixture as user_factory
register(NewsFactory)  # registers fixture as news_factory
