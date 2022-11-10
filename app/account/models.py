from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Игрок')
    city = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender_choice = (
        ('male', 'Мужской'),
        ('female', 'Женский')
    )   
    gender = models.CharField(choices=gender_choice,max_length=100, verbose_name='Пол')
    phone_number = models.IntegerField()


class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Администратор')
