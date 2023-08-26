import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .manager import AbstractUser, UserManager, BaseUserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    email = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Users(models.Model):
    user_uuid = models.UUIDField(primary_key=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    passcode = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number


class Tokens(models.Model):
    class Meta:
        db_table = 'token_blacklist_outstandingtoken'
        managed = False

    user_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    token = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class ScheduleClass(models.Model):

    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Payments(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Address = models.TextField()
    zip = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    bank_account_number = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
