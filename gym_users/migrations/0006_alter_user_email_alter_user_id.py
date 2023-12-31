# Generated by Django 4.2.4 on 2023-08-26 18:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gym_users', '0005_scheduleclass_alter_user_id_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('349b3e8a-154e-474f-b409-1b66dcd050b2'), primary_key=True, serialize=False, unique=True),
        ),
    ]
