# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns('core.views',
    url(r'^timeline/(?P<user_id>\d+)', 'timeline', name='timeline'),
)