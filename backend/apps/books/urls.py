"""Books app urls."""

from apps.generic.views import ReviewViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet, welcome

router = DefaultRouter()

router.register("", BookViewSet)
router.register("authors", AuthorViewSet)
router.register("reviews", ReviewViewSet)
# router.register("tags", views.TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # temporary:
    path("welcome/", welcome, name="welcome"),
]
