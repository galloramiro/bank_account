# Pytest
import pytest

# Django
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APIClient

# Factories
from accounts.tests.factories import CurrencyrFactory
from users.tests.factories import UserFactory


@pytest.fixture
def currencies():
    currency_1 = CurrencyrFactory(name='test_currency_1', is_active=True)
    currency_2 = CurrencyrFactory(name='test_currency_2', is_active=True)
    currency_3 = CurrencyrFactory(name='test_currency_3', is_active=True)
    currency_4 = CurrencyrFactory(name='test_currency_4', is_active=False)
    currency_5 = CurrencyrFactory(name='test_currency_5', is_active=False)
    return [currency_1, currency_2, currency_3, currency_4, currency_5]

@pytest.mark.django_db
def test_currencies_not_authenticated_list(currencies):
    client = APIClient()
    response = client.get(reverse("accounts:currencies-list"))
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()['detail'] == 'Authentication credentials were not provided.'


@pytest.mark.django_db
def test_currencies_list(client_logged, currencies):
    response = client_logged.get(reverse("accounts:currencies-list"))

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['count'] == 3


@pytest.mark.django_db
def test_currencies_create(client_logged):
    currency = dict(name='test_coin_23', is_active=True)
    response = client_logged.post(reverse("accounts:currencies-list"), currency)

    assert response.status_code == status.HTTP_201_CREATED
    
    response = client_logged.get(reverse("accounts:currencies-list"))

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['count'] == 1


@pytest.mark.django_db
def test_currencies_update(client_logged, currencies):
    url = reverse("accounts:currencies-detail", args=(currencies[0].id,))
    new_currency = dict(name='test_coin_23', is_active=True)
    response = client_logged.put(url, data=new_currency)
    
    assert response.status_code == status.HTTP_200_OK
    
    response = client_logged.get(url)

    assert response.json()['name'] == new_currency['name']


@pytest.mark.django_db
def test_currencies_delete(client_logged, currencies):
    url = reverse("accounts:currencies-detail", args=(currencies[0].id,))
    response = client_logged.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    response = client_logged.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
