# Pytest
import pytest

# Django
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APIClient

# Factories
from accounts.tests.factories import AccountFactory


@pytest.mark.django_db
def test_get_account_with_wrong_user(client_logged):
    account = AccountFactory()
    
    url = reverse("accounts:accounts-detail", args=(account.id,))
    response = client_logged.get(url)

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json()['detail'] == 'You do not have permission to perform this action.'


@pytest.mark.django_db
def test_get_account_with_correct_user(client_logged):
    user = client_logged.user_logged
    account = AccountFactory(user=user)
    

    url = reverse("accounts:accounts-detail", args=(account.id,))
    response = client_logged.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['user'] == user.id


@pytest.mark.django_db
def test_create_account_with_started_balance(client_logged):
    user = client_logged.user_logged

    data = dict(user=user.id, balance=10)
    response = client_logged.post(reverse("accounts:accounts-list"), data=data)
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()['balance'] == ['You are traing to start an account with a started balance.']


@pytest.mark.django_db
def test_delete_account(client_logged):
    account = AccountFactory(user=client_logged.user_logged)
    
    url = reverse("accounts:accounts-detail", args=(account.id,))
    response = client_logged.delete(url)
    
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    response = client_logged.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
