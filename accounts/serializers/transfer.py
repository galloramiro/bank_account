"""Transfer serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from accounts.models import Transfer


class TransferModelSerializer(serializers.ModelSerializer):
    """Transfer model serializer."""

    class Meta:
        """Meta class."""
        model = Transfer
        fields = ("amount", "date", "account_from", "account_to")

    def create(self, data):
        account_from = data['account_from']
        account_to = data['account_to']
        amount = data['amount']

        if account_from.balance - amount < 0:
            raise serializers.ValidationError("You do not have sufficient funds in your account")

        if account_from == account_to:
            raise serializers.ValidationError("You are traing to make a transfer to your own account")


        account_from.balance = account_from.balance - amount
        account_from.save()

        account_to.balance = account_to.balance + amount
        account_to.save()
        
        transfer = Transfer(**data)
        transfer.save()

        return transfer

    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("You cant send a negative amount")
        return amount
