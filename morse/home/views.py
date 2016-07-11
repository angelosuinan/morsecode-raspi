from django.shortcuts import render
import os
import threading
import multiprocessing
# Create your views here.

from django.views.generic import TemplateView, View

class Index(TemplateView):
    template_name = 'home/index.html'
    def get(self, request, *args, **kwargs):
        with open('run.txt', 'w+') as f:
            f.write("0")
        with open('api.txt' , 'w+') as f:
            f.write(" ")
        return render(request, self.template_name, )
