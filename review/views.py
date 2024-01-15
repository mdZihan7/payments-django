from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def customer(request):
    # return HttpResponse ("This shop products & service are best")
    return render(request, 'review/review.html')