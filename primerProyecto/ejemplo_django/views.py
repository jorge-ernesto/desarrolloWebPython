from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Esta es mi primera vista')

def ingreso(request):
    lista_elementos = [['Javier','Hilario','35'],['Dante','Arroyo','32'],['Luis','Velazco','33']]
    return render(request,'ejemplo_django/ingreso.html',{
        'usuarios':lista_elementos,
    })