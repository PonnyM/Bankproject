from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.

class UserAccounts(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=100,unique=True,primary_key=True)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_accounts"

    def __str__(self):
        return self.email

class EmailOtp(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now()> self.created_at+timedelta(minutes=3)
    


# Create your models here.
# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User_Accounts(models.Model):
#     email = models.EmailField(unique=True)
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     username = models.CharField(max_length=50, unique=True, default="tempuser")
#     password = models.CharField(max_length=50)
