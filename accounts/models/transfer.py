# Django
from django.db import models

# Models
from accounts.models import Account


class Transfer(models.Model):
    """Transfers model.

    This model represent the transfers between one account to the other
    """
    amount = models.DecimalField(decimal_places=5, max_digits=20)
    date = models.DateTimeField(auto_now=True)
    account_from = models.ForeignKey(Account, on_delete=models.RESTRICT, related_name='transfers_made')
    account_to = models.ForeignKey(Account, on_delete=models.RESTRICT, related_name='transfers_received')
