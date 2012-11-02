# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from asv_files.dj.admin import AsvFileInline
from demo.models import *
#---------------------------------------------------------------
#---------------------------------------------------------------
class ZakazAdmin(admin.ModelAdmin):
    inlines=(AsvFileInline,)
admin.site.register(Zakaz, ZakazAdmin)
#---------------------------------------------------------------
#---------------------------------------------------------------
