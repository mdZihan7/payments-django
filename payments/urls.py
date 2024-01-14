from django.urls import path
from . import views

urlpatterns = [
   
    path('pv/', views.home_page),
   
]