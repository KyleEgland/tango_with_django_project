#! python
#
# Rango app forms.py file
#
from django import forms
from django.contrib.auth.models import User
from rango.models import Page
from rango.models import Category
from rango.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them
        # Here, we are hiding the foreign key.  We can either include the
        # category field from the form,
        exclude = ('category',)
        # or specify the fields to include (i.e. not include the category
        # field)
        # fields = ('title', 'url', 'views')

    # Create a method that will add 'http://' if it doesn't begin with that or
    # 'https'.  This is a Django framework override method.
    def clean(self):
        # Grab form data from the ModelForm dictionary attribute 'cleaned_data'
        cleaned_data = self.cleaned_data
        # Use the ".get()" method provided by the dictionary to get a value
        # from the form - this case 'url'
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://' or 'https://',
        # them prepend with 'http://'
        if url and not url.startswith('http://'):
            if url and not url.startswith('https://'):
                url = 'http://' + url
                cleaned_data['url'] = url

                # Must always end the 'clean()'  method with this return,
                # (returning 'cleaned_data') otherwise changes won't save
                return cleaned_data
