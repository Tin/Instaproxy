from django.conf.urls.defaults import *
from settings import MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^instaproxy/', include('instaproxy.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^api/', include('core.urls')),
    (r'^front/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
