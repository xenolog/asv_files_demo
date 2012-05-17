# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django import forms
from asv_files.fields import *
from asv_utils.dj import reverse_lazy
from demo.models import Zakaz

#----------------------------------------------------------------
class Demo1Form(forms.Form):
    subject = forms.CharField(max_length=50)
    files = CTfilesFormField()
    files2 = CTfilesFormField()
#----------------------------------------------------------------
class Demo1(FormView):
    template_name = 'demo1.html'
    form_class    = Demo1Form
    success_url   = reverse_lazy('demo:success')

    def form_valid(self, form):
        ooo = Zakaz(title=form.cleaned_data['subject'])
        ooo.save()    # need for attaching files
        files = form.cleaned_data['files']
        for i in files.get_files():
            #print('*** file {frn} saved as {fn} ({fp}) and have ID:{id}'.format(
            #    frn = i.get_realname(),
            #    fn = i.get_filename(),
            #    fp = i.get_filepath(),
            #    id = i.get_fileid(),
            #))
            i.attach_to(ooo) # save and attach files through ContentTypes to ooo.
                             # ooo MUST be created and saved before it.
            #i.delete() # remove file from database and storage. not need if we call files.delete()
        files.delete() # remove session and her files from database and storage
        files2 = form.cleaned_data['files2']
        for i in files2.get_files():
            i.attach_to(ooo)
        files2.delete()
        #
        return HttpResponseRedirect(self.get_success_url())
#----------------------------------------------------------------
class OK(TemplateView):
    template_name = 'ok.html'
