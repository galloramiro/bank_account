# Django REST Framework
from accounts.permissions.transfers import IsTransfersAccountOwner
from rest_framework import mixins, viewsets

# Models
from accounts.models import Transfer

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from accounts.serializers import TransferModelSerializer


class TransferViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Transfer view set."""

    queryset = Transfer.objects.all()
    serializer_class = TransferModelSerializer
    permission_classes = (IsAuthenticated, IsTransfersAccountOwner)
