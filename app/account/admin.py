
from django.contrib import admin
from .models import User, Player, AdminUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'email', 'first_name', 'last_name')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'id',  'city', 'birthdate', 'gender', 'phone_number')


class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(User, UserAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(AdminUser, AdminUserAdmin)