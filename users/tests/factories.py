"""Users factory"""

# Factory
import factory

# Models
from users.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = factory.PostGenerationMethodCall("set_password", "default_password")
