from django.contrib import admin
from .models import *


@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'city', 'phone')  # Поля, які ви хочете відображати в списку
    search_fields = ('user__username', 'city', 'hobby')  # Поля для пошуку
    list_filter = ('city',)




