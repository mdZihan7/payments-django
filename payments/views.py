from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    # return HttpResponse ("Welcome")
    # offering = {'what' : 'kind of payment'}
    # kind = "cash or credit"
    # bank = "doha bank"
    # offering = {'a': kind, 'b': bank}
    # return render(request, 'payments/payments.html', context=offering)
 
    list = {'bank' : ['A','B','C','D']}
    return render(request, 'payments/payments.html', context=list)