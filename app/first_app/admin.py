from django.contrib import admin
from .models import Calendar, Category, Club, Rating, Trainer, News, NewsImages, Gallery, GalleryImages
from parler.admin import TranslatableTabularInline, TranslatableAdmin, TranslatableInlineModelAdmin


class CategoryAdmin(TranslatableAdmin):
    list_display = ('title', 'text')

class ClubAdmin(TranslatableAdmin):
    list_display = ('name', 'description', 'address', 'contacts', 'working_hours', 'images')
    
class TrainerAdmin(TranslatableAdmin):
    list_display = ('name', 'description', 'address', 'contacts', 'images')

class GalleryAdmin(TranslatableAdmin):
    list_display = ('main_image', 'date_added', 'title')

class GalleryImagesAdmin(TranslatableAdmin):
    list_display = ('gallery_id', 'images')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImages, GalleryImagesAdmin)


class CalendarAdmin(TranslatableAdmin):
    list_display = ('name', 'start_date', 'end_date')

class RatingAdmin(TranslatableAdmin):
    list_display = ('full_name', 'points')

class NewsImageAdminInline(admin.TabularInline):
    extra = 1
    model = NewsImages

@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    inlines = [NewsImageAdminInline, ]


admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Rating, RatingAdmin)
