#! python
# Rango App admin.py file
from django.contrib import admin
from rango.models import Category
from rango.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
