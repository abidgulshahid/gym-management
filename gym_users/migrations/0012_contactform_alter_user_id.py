# Generated by Django 4.2.4 on 2023-08-27 05:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gym_users', '0011_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c0212c7a-ba52-4712-82fe-b98bc09db1f5'), primary_key=True, serialize=False, unique=True),
        ),
    ]
