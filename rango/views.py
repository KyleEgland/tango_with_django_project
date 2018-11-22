#! python3
# Rango app views.py file
# from django.http import HttpResponse
from django.shortcuts import render
# Importing models in order to display
from rango.models import Category
from rango.models import Page
# Import forms for use
from rango.forms import CategoryForm
from rango.forms import PageForm


def add_category(request):
    form = CategoryForm()

    # An HTTP POST
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the ctegory is saved, we could give a confirmation
            # message but, since the most recent category added is on the index
            # page, direct the user back to the index page.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the
            # terminal.
            print(form.errors)
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass to the template rendering
    # engine
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?  If we can't,
        # the .get() method raises a DoesNotExist exception.  So the .get()
        # method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # NOTE: filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        # Add the results list to the template context under name pages.
        context_dict['pages'] = pages
        # Add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.  Dont' do
        # anything - the template will display the "no category" message for us
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the resonse and return it to the client
    return render(request, 'rango/category.html', context_dict)


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
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'pages': page_list}

    # Return a rendered response to send to the client.  We make use of the
    # shortcut function to make our lives easier.
    # The render function takes in the user's request, the template, and the
    # context dictionary.
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')
