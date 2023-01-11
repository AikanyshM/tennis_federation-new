from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


class Gender(models.TextChoices):
    male = _('мужской'), _('Мужской')
    female = _('женский'), _('Женский')


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name= _('Игрок'))
    email = models.EmailField(unique=True, blank=False)
    city = models.CharField(max_length=50, verbose_name= _('Город'))
    birthdate = models.DateField(verbose_name= _('Дата рождения'))  
    gender = models.CharField(choices=Gender.choices,max_length=100, verbose_name=_('Пол'))
    phone_number = models.BigIntegerField(verbose_name= _('Номер телефона'))

    def __str__(self):
        return self.user.first_name

class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Администратор'))

    
