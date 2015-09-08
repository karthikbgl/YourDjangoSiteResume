"""
Definition of urls for djangocon.
"""

from datetime import datetime
from django.conf.urls import patterns, url, include
from app import views 
from django.contrib import admin

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.home, name='home'),
    url(r'^health-finder/$', views.health_finder, name='health-finder'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^_admin/', include(admin.site.urls)),
)
