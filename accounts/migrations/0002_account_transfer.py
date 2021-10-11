# Generated by Django 3.2.8 on 2021-10-10 23:09

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=5, default=Decimal('0'), max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=5, max_digits=20)),
                ('date', models.DateTimeField(auto_now=True)),
                ('account_from', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='account_from', to='accounts.account')),
                ('account_to', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='account_to', to='accounts.account')),
            ],
        ),
    ]