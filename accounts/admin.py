"""User models admin."""

# Django
from django.contrib import admin

# Models
from accounts.models import (
    Account,
    Currency, 
    Transfer,
)


class AccountAdmin(admin.ModelAdmin):
    """User model admin."""

    list_display = ("user", "balance", "created_at")
    list_filter = ("user", "balance", "created_at")


class CurrencyAdmin(admin.ModelAdmin):
    """User model admin."""

    list_display = ("name", "is_active")
    list_filter = ("name", "is_active")


class TransferAdmin(admin.ModelAdmin):
    """User model admin."""

    list_display = ("amount", "date", "account_from", "account_to")
    list_filter = ("amount", "date", "account_from", "account_to")


admin.site.register(Account, AccountAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Transfer, TransferAdmin)
