"""Transactions permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsTransfersAccountOwner(BasePermission):
    """Allow access only to account owners."""

    def has_object_permission(self, request, view, transfers):
        """Check that the obj and user are equivalent"""
        if request.user == transfers.account_from.user:
            return True
        return False
