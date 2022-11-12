from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name = _("Заголовок"))
    text = models.TextField(verbose_name = _('Описание Федерации'))

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('place-detail', kwargs={'pk': self.pk})


class Club(models.Model):
    name = models.CharField(max_length=100, verbose_name = _("Название клуба"))
    description = models.CharField(max_length=255, verbose_name = _("Описание клуба"))
    address =   models.URLField(verbose_name = _("Адрес клуба"))
    contacts = models.CharField(max_length=100, verbose_name = _("Контакты"))
    working_hours = models.CharField(max_length=100, verbose_name = _("Часы работы"))
    Instagram = models.URLField(verbose_name= _("Instagram"))
    Facebook = models.URLField(verbose_name= _("Facebook"))
    images = models.ImageField(verbose_name = _("Фото клуба"))


    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=100, verbose_name= _("ФИО тренера"))
    description = models.CharField(max_length=255, verbose_name = _("Информация о тренере"))
    address =   models.CharField(max_length=100, verbose_name = _("Место работы"))
    contacts = models.CharField(max_length=100, verbose_name =  _("Контакты"))
    images = models.ImageField(verbose_name = _("Фото тренера"))


    def __str__(self):
        return self.name


class Calendar(models.Model):
    name = models.CharField(max_length=100, verbose_name= _('Название турнира'))
    date = models.DateField(verbose_name= _('Дата'))
    location = models.CharField(max_length=100, verbose_name= _('Город'))
    gender = (
        ('male', 'Мужчины'),
        ('female', 'Женщины')
    )
    age = (
        ('Under 14', 'До 14 лет'),
        ('14 and older', 'Старше 14 лет')
    )
    category_gender = models.CharField(choices=gender,max_length=100, verbose_name= _('Категория пол'))
    category_age = models.CharField(choices=age, max_length=100, verbose_name= _('Категория возраст'))


class Rating(models.Model):
    number = models.IntegerField(verbose_name= _('Место'))
    full_name = models.CharField(max_length=100, verbose_name= _('ФИО'))
    birth_date = models.DateField(verbose_name= _('Год рождения'))
    number_of_tournaments = models.IntegerField(verbose_name= _('Кол-во турниров'))
    gender = (
        ('male', 'Мужчины'),
        ('female', 'Женщины')
    )
    age = (
        ('Under 14', 'До 14 лет'),
        ('14 and older', 'Старше 14 лет')
    )
    category_gender = models.CharField(choices=gender,max_length=100, verbose_name= _('Категория пол'))
    category_age = models.CharField(choices=age, max_length=100, verbose_name= _('Категория возраст'))
    points = models.IntegerField(verbose_name= _('Очки'))


class News(models.Model):
    name = models.CharField(max_length=255, verbose_name= _('Краткое название'))
    date = models.DateField(auto_now_add=True, verbose_name= _('Дата создания'))
    description = models.TextField(verbose_name= _('Описание новости'))
    source = models.CharField(max_length=255, verbose_name= _('Источник'))
    main_photo = models.ImageField(verbose_name= _('Главное фото'), upload_to='news_main_image')

    def __str__(self):
        return self.name



class NewsImages(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name= _('Фотографии'), upload_to='news_image')

    def __str__(self):
        return self.news_id.name


class Gallery(models.Model):
    main_image = models.ImageField(upload_to ='gallery_main_image', verbose_name= _('Главное фото'))
    date_added = models.DateField(auto_now_add=True, verbose_name= _('Дата создания'))
    title = models.CharField(max_length=100, verbose_name= _("Заголовок новости")) 

    def __str__(self):
        return self.title

class GalleryImages(models.Model):
    gallery_id = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="gallery_images", verbose_name= _('Фотографии'))


class MainPage(models.Model):
    main_photo = models.ImageField(upload_to ='main_page_image', verbose_name= _('Главное фото'))
    whatsapp = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()

