from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, unique=True)
    password = models.CharField(max_length=120)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Ulanyjy'
        verbose_name_plural = 'Ulanyjylar'
    
    def __str__(self):
        return self.username
