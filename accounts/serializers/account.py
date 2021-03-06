"""Account serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from accounts.models import Account, transfer

# Serializers
from accounts.serializers.transfer import TransferModelSerializer


class AccountModelSerializer(serializers.ModelSerializer):
    """Account model serializer."""
    transfers = serializers.SerializerMethodField()

    class Meta:
        """Meta class."""
        model = Account
        fields = ("user", "balance", "transfers", "created_at")

    def validate_balance(self, balance):
        """
        Check the balance is 0.
        """
        if balance != 0:
            raise serializers.ValidationError("You are traing to start an account with a started balance.")
        return balance

    def get_transfers(self, account):
        made = account.transfers_made.all()
        received = account.transfers_received.all()
        transfers = made | received
        transfers = transfers.order_by('date')

        serializer = TransferModelSerializer(transfers, many=True)
        
        return serializer.data
