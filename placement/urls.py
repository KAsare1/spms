from django.urls import path, reverse

from . import views

urlpatterns = [
    path('', views.placement_save, name='form'),
]

