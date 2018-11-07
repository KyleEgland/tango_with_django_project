#! python
# Rango App admin.py file
from django.contrib import admin
from rango.models import Category
from rango.models import Page


admin.site.register(Category)
admin.site.register(Page)
