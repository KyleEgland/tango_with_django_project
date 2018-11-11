#! python3
# Rango app views.py file
# from django.http import HttpResponse
from django.shortcuts import render
# Importing models in order to display
from rango.models import Category


def index(request):
    # NOTE: Below left in for reference purposes
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    # context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy,
    #                 cupcake!'}

    # Query the database for a list of ALL categories currently stored.  Order
    # the categories by num likes in descending order.  Retrieve the top 5 only
    # - or all if less than 5.  Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Return a rendered response to send to the client.  We make use of the
    # shortcut function to make our lives easier.
    # The render function takes in the user's request, the template, and the
    # context dictionary.
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')
