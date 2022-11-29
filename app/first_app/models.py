from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields, TranslatedFieldsModel


User = get_user_model()


class Category(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100, verbose_name = _("Заголовок")),
        text = models.TextField(verbose_name = _('Описание Федерации'))
    )
    # def get_absolute_url(self):
    #     return reverse('place-detail', kwargs={'pk': self.pk})

    def __str__(self):
        title = self.safe_translation_getter('title', any_language=True)
        return title if title is not None else '(not translated)'


class Club(TranslatableModel):
    address_link = models.URLField(verbose_name = _("Ссылка на адрес клуба"))
    instagram = models.URLField(verbose_name= _("Instagram"))
    facebook = models.URLField(verbose_name= _("Facebook"))
    images = models.ImageField(verbose_name = _("Фото клуба"))
    translations = TranslatedFields(
        name = models.CharField(max_length=100, verbose_name = _("Название клуба")),
        description = models.CharField(max_length=255, verbose_name = _("Описание клуба")),
        address = models.CharField(max_length=255, verbose_name = _("Адрес клуба")),
        contacts = models.CharField(max_length=100, verbose_name = _("Контакты")),
        working_hours = models.CharField(max_length=100, verbose_name = _("Часы работы"))    
    )

    def __str__(self):
        name = self.safe_translation_getter('name', any_language=True)
        return name if name is not None else '(not translated)'


class Trainer(TranslatableModel):
    images = models.ImageField(verbose_name = _("Фото тренера"))
    translations = TranslatedFields(
        name = models.CharField(max_length=100, verbose_name= _("ФИО тренера")),
        description = models.CharField(max_length=255, verbose_name = _("Информация о тренере")),
        address =   models.CharField(max_length=100, verbose_name = _("Место работы")),
        contacts = models.CharField(max_length=100, verbose_name =  _("Контакты")),
    )

    def __str__(self):
        name = self.safe_translation_getter('name', any_language=True)
        return name if name is not None else '(not translated)'


class Gender(models.TextChoices):
    male = 'male', _('Male')
    female = 'female', _('Female')


class Age(models.TextChoices):
    under_14 = 'under_14', _('Under 14')
    older_14 = '14 and older', _('14 and older')


class Calendar(TranslatableModel):
    start_date = models.DateField(verbose_name= _('Дата начала турнира'))
    end_date = models.DateField(verbose_name= _('Дата окончания турнира'))
    translations = TranslatedFields(
        name = models.CharField(max_length=100, verbose_name= _('Название турнира')),
        location = models.CharField(max_length=100, verbose_name= _('Город')),
        category_gender = models.CharField(choices=Gender.choices,max_length=100, verbose_name= _('Категория пол')),
        category_age = models.CharField(choices=Age.choices, max_length=100, verbose_name= _('Категория возраст')),
        )

    def __str__(self):
        name = self.safe_translation_getter('name', any_language=True)
        return name if name is not None else '(not translated)'


class Rating(TranslatableModel):
    birth_date = models.DateField(verbose_name= _('Год рождения'))
    number_of_tournaments = models.IntegerField(verbose_name= _('Кол-во турниров'))
    points = models.IntegerField(verbose_name= _('Очки'))
    translations = TranslatedFields(
        full_name = models.CharField(max_length=100, verbose_name= _('ФИО')),
        category_gender = models.CharField(choices=Gender.choices,max_length=100, verbose_name= _('Категория пол')),
        category_age = models.CharField(choices=Age.choices, max_length=100, verbose_name= _('Категория возраст')),
        )


    def __str__(self):
        full_name = self.safe_translation_getter('full_name', any_language=True)
        return full_name if full_name is not None else '(not translated)'


class News(TranslatableModel):
    date = models.DateField(auto_now_add=True, verbose_name= _('Дата создания'))
    main_photo = models.ImageField(verbose_name= _('Главное фото'), upload_to='news_main_image')
    translations = TranslatedFields(
        name = models.CharField(max_length=255, verbose_name= _('Краткое название')),
        description = models.TextField(verbose_name= _('Описание новости')),
        source = models.CharField(max_length=255, verbose_name= _('Источник')),
    )

    def __str__(self):
        name = self.safe_translation_getter('name', any_language=True)
        return name if name is not None else '(not translated)'


class NewsImages(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name= _('Фотографии'), upload_to='news_image')

    def __str__(self):
        return self.news_id.name


class Gallery(TranslatableModel):
    main_image = models.ImageField(upload_to ='gallery_main_image', verbose_name= _('Главное фото'))
    date_added = models.DateField(auto_now_add=True, verbose_name= _('Дата создания'))
    translations = TranslatedFields(
        title = models.CharField(max_length=100, verbose_name= _("Название галерии")),
    )

    def __str__(self):
        title = self.safe_translation_getter('title', any_language=True)
        return title if title is not None else '(not translated)'


class GalleryImages(TranslatableModel):
    gallery_id = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="gallery_images", verbose_name= _('Фотографии'))


    def __str__(self):
        return self.gallery_id.name

class MainPage(models.Model):
    main_photo = models.ImageField(upload_to ='main_page_image', verbose_name= _('Главное фото'))
    whatsapp = models.BigIntegerField()
    facebook = models.URLField()
    instagram = models.URLField()


    def __str__(self):
        return self.main_photo
