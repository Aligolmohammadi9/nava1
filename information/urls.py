from django.contrib import admin
from django.urls import path
from .views import HomeView, register

app_name = 'information'

urlpatterns = [
    # path('', HomeView.as_view(), name='index')
    path('', register, name='index'),
    path('success', register, name='success')
    
]
