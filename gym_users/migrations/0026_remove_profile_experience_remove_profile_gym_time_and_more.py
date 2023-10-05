# Generated by Django 4.2.4 on 2023-09-30 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_users', '0025_alter_equipment_delivery_date_alter_profile_gym_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gym_time',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='memebership_date',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 30, 7, 14, 55, 842691)),
        ),
    ]