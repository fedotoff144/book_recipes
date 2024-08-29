from django.contrib.auth.models import AbstractUser
from django.db import models


# from django.

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='users_photo/', null=True, blank=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return (f'User(pk={self.pk}, '
                f'username: {self.username}, '
                f'email: {self.email})')

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
