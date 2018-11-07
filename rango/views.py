#! python3
# Rango app views.py file
# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response to send to the client.  We make use of the
    # shortcut function to make our lives easier.
    # The render function takes in the user's request, the template, and the
    # context dictionary.
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')
