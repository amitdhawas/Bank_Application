# Generated by Django 4.0.3 on 2023-03-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('Deposite', 'Deposite'), ('Withdrawal', 'Withdrawal'), ('Transfer', 'Transfer')], max_length=50),
        ),
    ]
