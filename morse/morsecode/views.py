from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from morsecode.test import Pimorse
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
    pass
