import pytest

# from apps.news.models import News
# from apps.news.tests.factories import NewsFactory

pytestmark = pytest.mark.django_db


def test_test():
    assert 1 == 1


# def test_news_get_absolute_url(news: News):
#     assert news.get_absolute_url() == f"/apps/news/news/{news.slug}/"
