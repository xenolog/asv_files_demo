# -*- coding: utf-8 -*-
from __future__ import unicode_literals
try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'ok/$', OK.as_view(), name='success'),
    url(r'^$', Demo1.as_view(), name='form1'),
)



