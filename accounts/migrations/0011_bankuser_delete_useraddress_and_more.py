# Generated by Django 4.0.3 on 2023-03-29 17:03

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0010_alter_useraddress_bankuser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.PositiveIntegerField()),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.DeleteModel(
            name='UserAddress',
        ),
        migrations.AlterField(
            model_name='userbankaccount',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='accounts.bankuser'),
        ),
    ]
