"""User models admin."""

# Django
from django.contrib import admin

# Models
from accounts.models import (
    Currency, 
    Transfer,
)


class CurrencyAdmin(admin.ModelAdmin):
    """User model admin."""

    list_display = ("name", "is_active")
    list_filter = ("name", "is_active")


admin.site.register(Currency, CurrencyAdmin)
