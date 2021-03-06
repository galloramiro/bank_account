"""Account permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Allow access only to account owners."""

    def has_object_permission(self, request, view, account):
        """Check that the obj and user are equivalent"""
        if request.user == account.user:
            return True
        return False
