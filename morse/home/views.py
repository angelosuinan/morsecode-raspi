from django.shortcuts import render
import os
import threading
import multiprocessing
# Create your views here.

from django.views.generic import TemplateView, View

class Index(TemplateView):
    template_name = 'home/index.html'
    def get(self, request, *args, **kwargs):
        path =os.path.join(os.path.expanduser('~'),'projects', 'morsecode-raspi',
                        'morse','raspicode','run.txt')
        with open(path, 'w+') as f:
            f.write("0")
        return render(request, self.template_name, )
