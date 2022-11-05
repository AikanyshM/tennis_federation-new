from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # REQUIRED_FIELDS = ['password', 'username']
    city = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender_choice = (
        ('male', 'Мужской'),
        ('female', 'Женский')
    )   
    gender = models.CharField(choices=gender_choice,max_length=100, verbose_name='Пол')
    phone_number = models.IntegerField()
