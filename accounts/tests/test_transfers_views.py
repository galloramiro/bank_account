# Pytest
from decimal import Decimal
from accounts.models.account import Account
import pytest

# Django
from django.urls import reverse

# Django REST Framework
from rest_framework import status

# Factories
from accounts.tests.factories import AccountFactory, TransferFactory
from users.tests.factories import UserFactory



@pytest.mark.django_db
def test_create_transfer_with_out_enought_balance(client_logged):
    account_from = AccountFactory(user=client_logged.user_logged, balance=Decimal("1000"))
    user_to = UserFactory()
    account_to = AccountFactory(user=user_to, balance=Decimal("500"))
    data = dict(
        amount=1500,
        account_from=account_from.id,
        account_to=account_to.id
    )

    response = client_logged.post(reverse("accounts:transfers-list"), data=data)
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == ["You do not have sufficient funds in your account"]


@pytest.mark.django_db
def test_create_transfer_with_negative_value(client_logged):
    account_from = AccountFactory(user=client_logged.user_logged, balance=Decimal("1000"))
    user_to = UserFactory()
    account_to = AccountFactory(user=user_to, balance=Decimal("500"))
    data = dict(
        amount=-500,
        account_from=account_from.id,
        account_to=account_to.id
    )

    response = client_logged.post(reverse("accounts:transfers-list"), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()['amount'] == ['You cant send a negative amount']


@pytest.mark.django_db
def test_create_transfer_circular_transfer(client_logged):
    account_from = AccountFactory(user=client_logged.user_logged, balance=Decimal("1000"))
    data = dict(
        amount=300,
        account_from=account_from.id,
        account_to=account_from.id,
    )

    response = client_logged.post(reverse("accounts:transfers-list"), data=data)
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == ["You are traing to make a transfer to your own account"]


@pytest.mark.django_db
def test_create_transfer(client_logged):
    account_from = AccountFactory(user=client_logged.user_logged, balance=Decimal("1000"))
    user_to = UserFactory()
    account_to = AccountFactory(user=user_to, balance=Decimal("500"))
    data = dict(
        amount=500,
        account_from=account_from.id,
        account_to=account_to.id
    )

    response = client_logged.post(reverse("accounts:transfers-list"), data=data)
    
    assert response.status_code == status.HTTP_201_CREATED
    assert Account.objects.get(id=account_from.id).balance == Decimal("500")
    assert Account.objects.get(id=account_to.id).balance == Decimal("1000")
