#! python3
#
# Rango urls.py file
#
from django.conf.urls import url
from rango import views

# A 'namespace' can be added to a URL configuration module in order to allow
# for multiple apps with the same url (I.e. two apps that each have an about
# page)
# app_name = 'rango'
# This would allow for pages to be accessed as follows:
# <a href="{% url 'rango:about' %}"About</a>
# The colon seperates the namespace (rango) from the page name

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
        views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
]
