from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from morsecode.test import Pimorse
from django.views.generic import View, TemplateView, DetailView

class Encode(View):
        template_name = 'morsecode/encode.html'
        def __init__(self):
            p = Pimorse()
            p.output_morse("a")
        #return HttpResponse("Hello, world. You're at the polls index.")
       # pimorse.output_morse("ADsd")
class Decode(View):
    pass
