from django.shortcuts import render
from django.urls import reverse
from .models import tareasExamen, usuariosFinal
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        #Validacion de informacion
        usuario_registrado = 0
        usuarios_totales = usuariosFinal.objects.all()

        for usuario in usuarios_totales:
            if usuario.usuario == nombreUsuario and usuario.contra == passwordUsuario:
                usuario_registrado = 1

        if usuario_registrado == 1:
            return HttpResponseRedirect(reverse('examenFinal:dashboard'))
        else:
            return render(request,'examenFinal/ingresar.html',{
                'mensaje':'Los datos ingresados son incorrectos',
            })
    return render(request,'examenFinal/ingresar.html')

def dashboard(request):
    return render(request,'examenFinal/dashboard.html',{
        'tareas_totales':tareasExamen.objects.all().order_by('id')
    })

def obtener_info_tarea(request):
    datoTarea = str(request.GET.get('tarea'))
    infoTarea = tareasExamen.objects.get(id=datoTarea)
    arregloTarea = [infoTarea.id,infoTarea.fechaCreacion,infoTarea.fechaEntrega,infoTarea.descripcion,infoTarea.estadoTarea]
    return JsonResponse({
        'dato':arregloTarea,
    })

def agregar_tarea(request):
    if request.method == 'POST':
        datos = json.load(request)
        fecha_creacion = datos.get('fecha_creacion')
        fecha_entrega = datos.get('fecha_entrega')
        descripcion = datos.get('descripcion')
        estado = datos.get('estado')
        print(fecha_creacion)
        print(fecha_entrega)
        print(descripcion)
        print(estado)
        tareasExamen(fechaCreacion=fecha_creacion,fechaEntrega=fecha_entrega,descripcion=descripcion,estadoTarea=estado).save()
        tarea = tareasExamen.objects.latest('id')
        id_tarea = str(tarea.id)
        return JsonResponse({
            'resp':'ok',
            'tarea':{
                'id_tarea':id_tarea,
                'fecha_creacion':tarea.fechaCreacion,
                'fecha_entrega':tarea.fechaEntrega,
                'descripcion':tarea.descripcion,
                'estado':tarea.estadoTarea,
            }
        })

def eliminar_tarea(request):
    datoTarea = str(request.GET.get('tarea'))
    infoTarea = tareasExamen.objects.get(id=datoTarea)
    arregloTarea = [infoTarea.id,infoTarea.fechaCreacion,infoTarea.fechaEntrega,infoTarea.descripcion,infoTarea.estadoTarea]
    infoTarea.delete()
    return JsonResponse({
        'dato':arregloTarea,
    })

def actualizar_tarea(request):
    if request.method == 'POST':
        datos = json.load(request)
        id_tarea = datos.get('id_tarea')
        fecha_creacion = datos.get('fecha_creacion')
        fecha_entrega = datos.get('fecha_entrega')
        descripcion = datos.get('descripcion')
        estado = datos.get('estado')
        print(id_tarea)
        print(fecha_creacion)
        print(fecha_entrega)
        print(descripcion)
        print(estado)
        tarea = tareasExamen.objects.get(id=id_tarea)
        tarea.fechaCreacion = fecha_creacion
        tarea.fechaEntrega = fecha_entrega
        tarea.descripcion = descripcion
        tarea.estadoTarea = estado
        tarea.save()
        return JsonResponse({
            'resp':'ok',
            'tarea':{
                'id_tarea':id_tarea,
                'fecha_creacion':tarea.fechaCreacion,
                'fecha_entrega':tarea.fechaEntrega,
                'descripcion':tarea.descripcion,
                'estado':tarea.estadoTarea,
            }
        })