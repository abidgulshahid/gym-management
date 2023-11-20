# Generated by Django 4.2.4 on 2023-11-20 16:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_users', '0037_remove_payments_address_remove_payments_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleclass',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 20, 16, 35, 0, 83007)),
        ),
    ]
