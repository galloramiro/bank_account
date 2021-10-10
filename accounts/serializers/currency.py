"""Currency serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from accounts.models import Currency


class CurrencyModelSerializer(serializers.ModelSerializer):
    """Currency model serializer."""

    class Meta:
        """Meta class."""
        model = Currency
        fields = ("name", "is_active")
