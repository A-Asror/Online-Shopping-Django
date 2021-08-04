from django.contrib import admin
from .models import *


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'status')
    list_display_links = ('name', 'category', 'created_at')
    search_fields = ('name', )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status')
    list_display_links = ('name', 'email')
    search_fields = ('name', )


@admin.register(ChekOut)
class CheckOut(admin.ModelAdmin):
    list_display = ('name', 'company', 'sity', 'phone')
    list_display_links = ('name',)
    search_fields = ('name', 'company', 'sity')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'status')
    list_display_links = ('name', )
    search_fields = ('name', 'city')


# admin.site.register(Products, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
# admin.site.register(Blog)
# admin.site.register(Contact)
