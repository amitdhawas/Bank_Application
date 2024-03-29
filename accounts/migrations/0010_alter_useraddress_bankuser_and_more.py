# Generated by Django 4.0.3 on 2023-03-29 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_rename_user_useraddress_bankuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='bankuser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='street_address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userbankaccount',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='BankUsers',
        ),
    ]
