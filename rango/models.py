#! python
# Rango App Models file
from django.db import models


class Category(models.Model):

    # Specify the field(s), associated types, and any required or optional
    # parameters
    name = models.CharField(max_length=128, unique=True)

    # This will allow the name of the class to be correctly displayed when it
    # is pluralized
    class Meta:
        verbose_name_plural = 'Categories'

    # Generate a string representation of the class
    def __str__(self):
        return self.name


class Page(models.Model):

    # Specify the field(s), associated types, and any required or optional
    # parameters
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    # Generate a string representation of the class
    def __str__(self):
        return self.title
