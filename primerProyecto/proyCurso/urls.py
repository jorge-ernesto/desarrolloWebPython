from . import views
from django.urls import path

app_name='proyCurso'

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('vistaProd/<str:ind>',views.vistaProd,name='vistaProd'),
    path('eliminarProd/<str:ind>',views.eliminarProd,name='eliminarProd')
]