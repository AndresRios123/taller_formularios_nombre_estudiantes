from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario_asistencia, name='formulario'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]