# Django
from django.db import models

# Models
from users.models import User


class Transfer(models.Model):
    """Transfers model.

    This model represent the transfers between one account to the other
    """
    amount = models.DecimalField(decimal_places=5, max_digits=20)
    date = models.DateTimeField(auto_now=True)
    user_from = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='user_from')
    user_to = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='user_to')
