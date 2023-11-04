from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    isim = "Cesur"
    context = {"isim": isim}
    return render(request, 'index.html', context)
    #return HttpResponse("Deneme")