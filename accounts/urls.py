"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from accounts.views import CurrencyViewSet


router = DefaultRouter()
router.register(r"currencies", CurrencyViewSet, basename="currencies")

urlpatterns = [
    path("", include(router.urls))
]
