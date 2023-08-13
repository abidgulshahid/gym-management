import uuid

from django.db import models
from .manager import AbstractUser, UserManager, BaseUserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    email = models.EmailField(max_length=100, unique=True)
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
