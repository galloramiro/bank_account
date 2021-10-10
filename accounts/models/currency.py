# Django
from django.db import models


class Currency(models.Model):
    """Currency model.

    This represent the type of currency that the accound will use
    """
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
