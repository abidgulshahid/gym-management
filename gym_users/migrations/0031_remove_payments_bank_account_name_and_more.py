# Generated by Django 4.2.4 on 2023-11-19 05:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_users', '0030_alter_equipment_delivery_date_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='bank_account_name',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='bank_account_number',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='email',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='zip',
        ),
        migrations.AddField(
            model_name='payments',
            name='status',
            field=models.CharField(blank=True, choices=[('Advance', 'Advance'), ('Monthly', 'Monthly')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='total_amount',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 19, 5, 44, 34, 652673)),
        ),
    ]
