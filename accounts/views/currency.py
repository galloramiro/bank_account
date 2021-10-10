# Django REST Framework
from rest_framework import viewsets

# Models
from accounts.models import Currency

# Permissions
from rest_framework.permissions import (
    IsAuthenticated
)

# Serializers
from accounts.serializers import CurrencyModelSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    """Currency view set."""

    queryset = Currency.objects.filter(is_active=True)
    serializer_class = CurrencyModelSerializer
    permission_classes = (IsAuthenticated,)
