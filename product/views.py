from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cake(request):
    # return HttpResponse ("Cake is yummy")
    return render(request, 'product/product.html')