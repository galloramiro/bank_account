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


class TransferAdmin(admin.ModelAdmin):
    """User model admin."""

    list_display = ("amount", "date", "user_from", "user_to")
    list_filter = ("amount", "date", "user_from", "user_to")


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Transfer, TransferAdmin)
