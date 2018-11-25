#! python
# Rango App Models file
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required.  Links UserProfile to a User model instance
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return something meaningful
    def __str__(self):
        return self.user.username


class Category(models.Model):

    # Specify the field(s), associated types, and any required or optional
    # parameters
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

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
