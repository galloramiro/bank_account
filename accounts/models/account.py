from decimal import Decimal

# Django
from django.db import models
from django.db.models.fields import DateTimeField

# Models
from users.models import User


class Account(models.Model):
    """Account model.

    This model group the transfers between users
    """
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    balance = models.DecimalField(decimal_places=5, max_digits=20, default=Decimal('0'))
    created_at = DateTimeField(auto_now_add=True)
