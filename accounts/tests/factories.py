"""Account factory"""
from decimal import Decimal

# Factory
import factory

# Models
from accounts.models import (
    Account,
    Currency,
    Transfer,
)

# Factories
from users.tests.factories import UserFactory


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    user = factory.SubFactory(UserFactory)
    balance = Decimal('0')


class CurrencyrFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Currency

    name = factory.Faker("currency_name")
    is_active = True


class TransferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transfer

    amount = Decimal('1')
    account_from = factory.SubFactory(UserFactory)
    account_to = factory.SubFactory(UserFactory)
