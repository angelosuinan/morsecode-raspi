from django.shortcuts import render
from home.button import InputMorse
import threading
import multiprocessing
# Create your views here.

from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'home/index.html'
    def get(self, request, *args, **kwargs):
        t= multiprocessing.Process(target = self.in_morse)
        t.start()
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        # threading:w
        return render(request, 'morsecode/decode.html')
    def in_morse(self):
        i = InputMorse(2)
        i.begin()
