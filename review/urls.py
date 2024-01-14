from django.urls import path
from . import views 

urlpatterns = [
   
    path('cr/', views.customer),
   
]