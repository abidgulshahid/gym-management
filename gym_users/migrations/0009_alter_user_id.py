# Generated by Django 4.2.4 on 2023-08-27 04:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gym_users', '0008_scheduleclass_user_alter_payments_user_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a56628d0-4bd9-43a6-8773-fd55b1de536e'), primary_key=True, serialize=False, unique=True),
        ),
    ]
