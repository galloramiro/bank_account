# Pytest
import pytest

# Django
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APIClient

# Factories
from users.tests.factories import UserFactory

# Serializers
from users.serializers import UserSignUpSerializer


@pytest.mark.django_db
def test_signup_view():
    client = APIClient()
    response = client.post(
        reverse("users:users-signup"),
        dict(
            email="fake@mail.com", 
            username="test_user",
            phone_number="+541122223333",
            password="fakepass455",
            password_confirmation="fakepass455",
            first_name="Adalberto",
            last_name="Paredes",
        )
    )

    expected_response = [dict(
        email="fake@mail.com", 
        username="test_user",
        phone_number="+541122223333",
        first_name="Adalberto",
        last_name="Paredes",
    )]
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == expected_response


@pytest.mark.django_db
def test_signup_view_password_confirmation():
    client = APIClient()
    response = client.post(
        reverse("users:users-signup"),
        dict(
            email="fake@mail.com", 
            username="test_user",
            phone_number="+541122223333",
            password="fakepass455",
            password_confirmation="otherfakepass222",
            first_name="Adalberto",
            last_name="Paredes",
        )
    )

    expected_response = dict(non_field_errors=["Passwords don't match."])
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == expected_response


@pytest.mark.django_db
def test_login_view():
    user = UserFactory(email="user@mail.com", is_verified=True)
    client = APIClient()
    response = client.post(
        reverse("users:users-login"),
        dict(
            email=user.email, 
            password="default_password",
        )
    )
    
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_login_view_with_unverified_user():
    user = UserFactory(email="user@mail.com")
    client = APIClient()
    response = client.post(
        reverse("users:users-login"),
        dict(
            email=user.email, 
            password="default_password",
        )
    )

    expected_response = dict(non_field_errors=["Account is not active yet"])

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == expected_response


@pytest.mark.django_db
def test_login_view_with_wrong_credentials():
    user = UserFactory(email="user@zzmail.com", is_verified=True)
    client = APIClient()
    response = client.post(
        reverse("users:users-login"),
        dict(
            email=user.email, 
            password="default_rassword",
        )
    )

    expected_response = dict(non_field_errors=["Invalid credentials"])

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == expected_response


@pytest.mark.django_db
def test_verify_view():
    user = UserFactory(email="user@zzmail.com", is_verified=True)
    token = UserSignUpSerializer().gen_verification_token(user)

    client = APIClient()
    response = client.post(
        reverse("users:users-verify"),
        dict(
            email=user.email,
            password="default_password",
            token=token
        )
    )

    expected_response = dict(message="Congratulations, now go start use the app!")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response
    


@pytest.mark.django_db
def test_verify_view_with_wrong_token():
    user = UserFactory(email="user@zzmail.com", is_verified=True)
    UserSignUpSerializer().gen_verification_token(user)

    client = APIClient()
    response = client.post(
        reverse("users:users-verify"),
        dict(
            email=user.email,
            password="default_password",
            token="token"
        )
    )

    expected_response = dict(token=["Invalid Token"])

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == expected_response
