# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.program_list,
        name='program_list'
    ),
    url(
        regex=r'(?P<program_slug>[-\w]+)/$',
        view=views.program_detail,
        name='program_detail'
    ),
    url(
        regex=r'(?P<program_slug>[-\w]+)/entry/(?P<programentryid>\d+)/$',
        view=views.program_entry,
        name='program_entry'
    ),
    url(
        regex=r'(?P<program_slug>[-\w]+)/(?P<exercise_slug>[-\w]+)$',
        view=views.exercise_detail,
        name='exercise_detail'
    ),
    url(
        regex=r'(?P<program_slug>[-\w]+)/entry/(?P<programentryid>\d+)/(?P<exercise_slug>[-\w]+)/(?P<exerciseentryid>\d+)/$',
        view=views.exercise_entry,
        name='exercise_entry'
    ),
]
