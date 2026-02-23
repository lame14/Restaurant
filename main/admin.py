from django.contrib import admin
from .models import Booking, MenuItem, Review

# Регистрация модели бронирования в админке
admin.site.register(Booking)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('title', 'description')

    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'text')