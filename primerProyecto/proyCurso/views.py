from django.shortcuts import render
from .models import producto
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse

# Create your views here.

def dashboard(request):
    productos_totales = producto.objects.all()
    return render(request,'proyCurso/dashboard.html',{
        'productos_totales':productos_totales
    })

def vistaProd(request,ind):
    producto_seleccionado = producto.objects.get(id=ind)
    return render(request,'proyCurso/vistaProd.html',{
        'producto_seleccionado':producto_seleccionado
    })

def eliminarProd(request,ind):
    producto_eliminar = producto.objects.get(id=ind)
    producto_eliminar.delete()
    return HttpResponseRedirect(reverse('proyCurso:dashboard'))

def obtenerInfo(request):
    datoProducto = str(request.GET.get('producto'))
    infoProducto = producto.objects.get(id=datoProducto)
    arregloProducto = [infoProducto.nombre,infoProducto.precio,infoProducto.descripcion,infoProducto.estado,infoProducto.stock]
    return JsonResponse({
        'dato':arregloProducto,
    })