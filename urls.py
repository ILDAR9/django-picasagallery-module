# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
                       (r'^$', 'picasagallery.views.gallery'),
                       (r'^album/(?P<album_id>\d+)/$', 'picasagallery.views.album_list'),
                       )
