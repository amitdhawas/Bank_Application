# Generated by Django 4.0.3 on 2023-03-23 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_delete_bankaccounttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_type',
            field=models.CharField(help_text='Enter Account Type Current/Savings', max_length=100),
        ),
    ]