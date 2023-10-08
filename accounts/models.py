from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     otp = models.Charfield(max_length=7, null=True, blank=True)
#     is_verified = models.BooleanField(default=False)
#     # email_verification_token = models.Charfield(max_length =200, null =True, blank=True)
#     # forgot_password_token = models.models.CharField(null=True, blank=True, max_length=50)