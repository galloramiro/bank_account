# Django REST Framework
from accounts.permissions.account import IsAccountOwner
from rest_framework import mixins, viewsets

# Models
from accounts.models import Account

# Permissions
from rest_framework.permissions import (
    IsAuthenticated
)

# Serializers
from accounts.serializers import AccountModelSerializer


class AccountViewSet(
    mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.DestroyModelMixin, viewsets.GenericViewSet,
    ):
    """Account view set."""

    queryset = Account.objects.all()
    serializer_class = AccountModelSerializer

    def get_permissions(self):
        """Assign permissions based on actions."""
        permissions = [IsAuthenticated]

        if self.action in ['retrieve', 'destroy']:
            permissions.append(IsAccountOwner)
        return [permission() for permission in permissions]
