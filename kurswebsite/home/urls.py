from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # def ile tanımladığmz fonk un adı "indeks" olan işte iks harfim yok
]