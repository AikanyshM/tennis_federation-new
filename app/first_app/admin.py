from django.contrib import admin
from .models import Calendar, Category, Club, Rating, Trainer, News, NewsImages, Gallery, GalleryImages, MainPage, OfficialPartner, InformationalPartners, SponsorsAndPartners
from parler.admin import TranslatableTabularInline, TranslatableAdmin, TranslatableInlineModelAdmin


class CategoryAdmin(TranslatableAdmin):
    list_display = ('title', 'text')

class ClubAdmin(TranslatableAdmin):
    list_display = ('name', 'description', 'address', 'contacts', 'working_hours', 'images')
    
class TrainerAdmin(TranslatableAdmin):
    list_display = ('name', 'description', 'address', 'contacts', 'images')

class GalleryImagesAdminInline(admin.TabularInline):
    extra = 1
    model = GalleryImages


@admin.register(Gallery)
class GalleryAdmin(TranslatableAdmin):
    inlines = [GalleryImagesAdminInline, ]

class CalendarAdmin(TranslatableAdmin):
    list_display = ('name', 'start_date', 'end_date', 'location')

class RatingAdmin(TranslatableAdmin):
    list_display = ('full_name', 'points', 'birth_date', 'category_gender', 'number_of_tournaments',
    'category_age')

class NewsImageAdminInline(admin.TabularInline):
    extra = 1
    model = NewsImages

@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    inlines = [NewsImageAdminInline, ]

class MainPageAdmin(admin.ModelAdmin):
    list_display = ('main_photo', 'whatsapp', 'facebook', 'instagram')


class OfficialPartnerAdmin(admin.ModelAdmin):
    list_display = ('images',)

class SponsorsAndPartnersAdmin(admin.ModelAdmin):
    list_display = ('images',)

class InformationalPartnerAdmin(admin.ModelAdmin):
    list_display = ('images',)



admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(MainPage, MainPageAdmin)
admin.site.register(OfficialPartner, OfficialPartnerAdmin)
admin.site.register(SponsorsAndPartners, SponsorsAndPartnersAdmin)
admin.site.register(InformationalPartners, InformationalPartnerAdmin)

