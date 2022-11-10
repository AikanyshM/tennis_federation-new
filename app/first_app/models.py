from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Заголовок")
    text = models.TextField(verbose_name = 'Описание Федерации')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('place-detail', kwargs={'pk': self.pk})


class Club(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Название клуба")
    description = models.CharField(max_length=255, verbose_name = "Описание клуба")
    address =   models.URLField(verbose_name = "Адрес клуба")
    contacts = models.CharField(max_length=100, verbose_name = "Контакты")
    working_hours = models.CharField(max_length=100, verbose_name = "Часы работы")
    Instagram = models.URLField(verbose_name="Instagram")
    Facebook = models.URLField(verbose_name="Facebook")
    images = models.ImageField(verbose_name = "Фото клуба")


    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО тренера")
    description = models.CharField(max_length=255, verbose_name = "Информация о тренере")
    address =   models.CharField(max_length=100, verbose_name = "Место работы")
    contacts = models.CharField(max_length=100, verbose_name = "Контакты")
    images = models.ImageField(verbose_name = "Фото тренера")


    def __str__(self):
        return self.name


class Calendar(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название турнира')
    date = models.DateField(verbose_name='Дата')
    location = models.CharField(max_length=100, verbose_name='Город')
    gender = (
        ('male', 'Мужчины'),
        ('female', 'Женщины')
    )
    age = (
        ('Under 14', 'До 14 лет'),
        ('14 and older', 'Старше 14 лет')
    )
    category_gender = models.CharField(choices=gender,max_length=100, verbose_name='Категория пол')
    category_age = models.CharField(choices=age, max_length=100, verbose_name='Категория возраст')


class Rating(models.Model):
    number = models.IntegerField(verbose_name='Место')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    birth_date = models.DateField(verbose_name='Год рождения')
    number_of_tournaments = models.IntegerField(verbose_name='Кол-во турниров')
    gender = (
        ('male', 'Мужчины'),
        ('female', 'Женщины')
    )
    age = (
        ('Under 14', 'До 14 лет'),
        ('14 and older', 'Старше 14 лет')
    )
    category_gender = models.CharField(choices=gender,max_length=100, verbose_name='Категория пол')
    category_age = models.CharField(choices=age, max_length=100, verbose_name='Категория возраст')
    points = models.IntegerField()


class News(models.Model):
    name = models.CharField(max_length=255, verbose_name='Краткое название')
    date = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Описание новости')
    source = models.CharField(max_length=255, verbose_name='Источник')
    main_photo = models.ImageField(verbose_name='Главное фото', upload_to='news_main_image')

    def __str__(self):
        return self.name



class NewsImages(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Фотографии', upload_to='news_image')

    def __str__(self):
        return self.news_id.name


class Gallery(models.Model):
    main_image = models.ImageField(upload_to ='gallery_main_image')
    date_added = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, verbose_name="Заголовок новости") 

    def __str__(self):
        return self.title

class GalleryImages(models.Model):
    gallery_id = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="gallery_images")


class MainPage(models.Model):
    main_photo = models.ImageField(upload_to ='main_page_image')
    whatsapp = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()

