"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from accounts.views import (
    AccountViewSet,
    CurrencyViewSet,
    TransferViewSet
)


router = DefaultRouter()
router.register(r"accounts", AccountViewSet, basename="accounts")
router.register(r"currencies", CurrencyViewSet, basename="currencies")
router.register(r"transfers", TransferViewSet, basename="transfers")


urlpatterns = [
    path("", include(router.urls))
]
