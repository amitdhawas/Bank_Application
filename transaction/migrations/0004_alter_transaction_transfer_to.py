# Generated by Django 4.0.3 on 2023-04-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_transaction_transfer_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transfer_to',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
