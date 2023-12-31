# Generated by Django 4.1.10 on 2023-08-03 12:23

from django.db import migrations
import requests

# add currencies from api.exchangerate
def add_currencies(apps, schema_editor):
    URL = 'https://api.exchangerate.host/symbols'
    page = requests.get(URL).json()
    currencies = page['symbols']

    Currency = apps.get_model('finance_tracker', 'Currency')

    currencies_list = []
    for currency in currencies.values():
        currencies_list.append(Currency(name = currency['description'],
                                        code = currency['code'],
                                        symbol = currency['code']))
    
    Currency.objects.bulk_create(currencies_list)


class Migration(migrations.Migration):

    dependencies = [
        ('finance_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_currencies)
    ]
