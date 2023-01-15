import pytest

from apps.news.models import News

pytestmark = pytest.mark.django_db


def test_new_news_build(news_factory):
    count_before = News.objects.all().count()
    news = news_factory.build()
    count_after = News.objects.all().count()
    assert count_after == count_before
    assert news.title
    assert news.user


def test_new_news_create(news_factory):
    count_before = News.objects.all().count()
    news = news_factory.create()
    count_after = News.objects.all().count()
    assert count_after == count_before + 1
    assert news.title
    assert news.user


# to be done later
# def test_news_get_absolute_url(news: News):
#     assert news.get_absolute_url() == f"/apps/news/news/{news.slug}/"
