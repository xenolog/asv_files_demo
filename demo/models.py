# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.timezone import *

#---------------------------------------------------------------
#---------------------------------------------------------------
class Zakaz(models.Model):
    active = models.BooleanField(default=True)
    title  = models.CharField(max_length=128, blank=True)
    de     = models.DateTimeField(auto_now_add=True)
    lm     = models.DateTimeField(auto_now=True)
    #----------
    def __unicode__(self):
        d = make_naive(self.de,get_current_timezone()).strftime('%Y-%m-%d %H:%M:%S')
        return smart_unicode('({date})  {title}'.format(
            title=self.title or '-unnamed-',
            date=d
        ))
    class Meta:
        ordering = ('de',)
        verbose_name='заказ'
        verbose_name_plural='заказы'
#-------------------------------------------------------------------
#-------------------------------------------------------------------
