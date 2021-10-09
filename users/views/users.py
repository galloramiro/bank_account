"""Users views."""

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from users.models import User

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

# Serializers
from users.serializers import (
    AccountVerificationSerializer,
    UserLoginSerializer,
    UserModelSerializer, 
    UserSignUpSerializer,
)


class UserViewSet(viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification.
    """

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = "username"

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ["signup", "login", "verify"]:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]
    
    @action(detail=False, methods=["post"])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data,
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=["post"])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = dict(
            status=UserModelSerializer(user).data,
            acces_token=token,
        )
        return Response(data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["post"])
    def verify(self, request):
        """User verification."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = dict(message="Congratulations, now go start use the app!")
        return Response(data, status=status.HTTP_200_OK)
