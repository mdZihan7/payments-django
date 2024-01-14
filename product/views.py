from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def cake(request):
    return HttpResponse ("Cake is yummy")