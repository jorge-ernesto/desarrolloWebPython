from . import views
from django.urls import path

app_name='proyCurso'

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('vistaProd',views.vistaProd,name='vistaProd'),
]