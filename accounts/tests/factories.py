"""Account factory"""

# Factory
import factory

# Models
from accounts.models import Currency


class CurrencyrFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Currency

    name = factory.Faker("currency_name")
    is_active = True
