from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from raspicode.test import Pimorse
from raspicode.button import InputMorse
from django.views.generic import View, TemplateView, DetailView
from django.shortcuts import render
import threading
class Encode(View):
    template_name = 'morsecode/encode.html'
       # def __init__(self):
        #    p = Pimorse()
         #   p.output_morse("a")
    def get(self, request, *args):

        return render(request, self.template_name,)
    def post(self, request):

        msg = request.POST.get("txtNewMsg")

        t = threading.Thread(target=self.out_morse, args=[msg])

        t.setDaemon(False)
        t.start()
        return render(request, self.template_name)

    def out_morse(self,msg):
        p= Pimorse()
        p.output_morse(msg)

class Decode(View):
    template_name = 'morsecode/decode.html'
    def get(self, request, *args):
        return render(request, self.template_name,)
    def in_morse(self, request, *args):
        i = InputMorse()
        i.begin()
