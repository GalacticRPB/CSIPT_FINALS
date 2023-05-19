from django.urls import path
from . import views

urlpatterns = [
    path('', views.residentrecords, name='residentrecords'),
    path('register/', views.residentform, name='registerresident'),
    path('edit/<resID>', views.editresident, name='editresident'),
    path('delete/<resID>', views.deleteresident, name='deleteresident'),
]