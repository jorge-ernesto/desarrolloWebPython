from django.shortcuts import render
from .models import producto

# Create your views here.

def dashboard(request):
    productos_totales = producto.objects.all()
    return render(request,'proyCurso/dashboard.html',{
        'productos_totales':productos_totales
    })

def vistaProd(request,ind):
    return render(request,'proyCurso/vistaProd.html')