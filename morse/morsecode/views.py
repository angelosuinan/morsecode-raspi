from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from raspicode.test import Pimorse

def index(request):
        pimorse=Pimorse()
        pimorse.output_morse("a")
        return HttpResponse("Hello, world. You're at the polls index.")
        pimorse.output_morse("ADsd")
