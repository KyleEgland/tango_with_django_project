#! python
# Script for populating the Rango App in the Tango with Django project
# The below two lines are necessary in order to work with the Django models
# that were created.  The django.setup() must be run before the models can be
# imported and manipulated
import django
django.setup()
from rango.models import Category
from rango.models import Page


def populate():
    # First, we will create lists of dictionaries containing the pages we want
    # to add into each category.
    # Then we will create a dictionary of dictionaires for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/3/tutorial/"},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.11/intro/tutorial01/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"}
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"}
    ]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages}}

    # If you want to add more categories or pages, add them to the dictionaries
    # above

    # The code below goes through the category dictionary (cats), then adds
    # each category, and then adds all the associated pages for that category.
    # If you are using Python 2.x then use cats.iteritems(); see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/ for more
    # information about how to iterate over a dictionary properly.

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    # Print out the categories we have added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    # the get_or_create() method is used as it will check to see if the entry
    # has been created or not before attemmpting to create it.
    # This method will return a tuple of (object, created) - object is a ref to
    # the model instance that the method creates if the db entry was not found,
    # created is a bool
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


# Start execution here
if __name__ == '__main__':
    print("[*] Starting Rango population script...")
    populate()
