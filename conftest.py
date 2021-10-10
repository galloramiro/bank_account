# Pytest
import pytest

# Django
from django.urls import reverse

# Django REST Framework
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

# Models
from users.models import User
from users.tests.factories import UserFactory


class LoggedAPIClient(APIClient):
    user_logged: User


@pytest.fixture
def client_logged() -> LoggedAPIClient:
    user =  UserFactory(email="user@mail.com", password="default_password", is_verified=True)
    client = LoggedAPIClient()
    
    response = client.post(
        reverse("users:users-login"),
        dict(email=user.email, password="default_password",)
    )
    token = response.json()['acces_token']
    
    client.login(username=user.email, password='default_password')
    client.user_logged = user

    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    return client
