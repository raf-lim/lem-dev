"""News app urls."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("news", views.NewsViewSet)
router.register("comments", views.CommentViewSet)
router.register("tags", views.TagViewSet)
# router.register("files", views.FileViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # temporary:
    path("welcome/", views.welcome, name="welcome"),
]
