"""Account serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from accounts.models import Account


class AccountModelSerializer(serializers.ModelSerializer):
    """Account model serializer."""

    class Meta:
        """Meta class."""
        model = Account
        fields = ("user", "balance", "created_at")

    def validate_balance(self, balance):
        """
        Check the balance is 0.
        """
        if balance != 0:
            raise serializers.ValidationError("You are traing to start an account with a started balance.")
        return balance
