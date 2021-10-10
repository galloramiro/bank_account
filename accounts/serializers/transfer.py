"""Currency serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from accounts.models import Transfer


class TransferModelSerializer(serializers.ModelSerializer):
    """Transfer model serializer."""

    class Meta:
        """Meta class."""
        model = Transfer
        fields = ("amount", "date", "user_from", "user_to")
