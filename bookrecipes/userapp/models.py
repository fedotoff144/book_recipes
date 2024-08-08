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

    # password = models.CharField(max_length=50)

    def __str__(self):
        return (f'name: {self.name}, '
                f'email: {self.email}, '
                f'gender: {self.gender if self.gender else "NULL"}, '
                f'birthday: {self.birthday if self.birthday else "NULL"}, '
                f'photo: {"YES" if self.photo else "NULL"}')
