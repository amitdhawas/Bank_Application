# Generated by Django 4.0.3 on 2023-03-23 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userbankaccount_account_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BankAccountType',
        ),
    ]