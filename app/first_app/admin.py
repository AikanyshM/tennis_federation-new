from django.contrib import admin
from .models import Calendar, Category, Club, Rating, Trainer, News, NewsImages, Gallery, GalleryImages


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'contacts', 'working_hours', 'images')
    
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'contacts', 'images')

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('main_image', 'date_added', 'title')

class GalleryImagesAdmin(admin.ModelAdmin):
    list_display = ('gallery_id', 'images')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImages, GalleryImagesAdmin)


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('number', 'full_name', 'points')
    
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')


class NewsImageAdmin(admin.ModelAdmin):
    list_display = ('news_id', 'photo')


admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(NewsImages, NewsImageAdmin)