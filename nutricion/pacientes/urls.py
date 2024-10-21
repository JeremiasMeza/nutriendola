from django.urls import path
from . import views
from .views import agregar_consulta

urlpatterns = [
    path('', views.vista_principal, name='vista_principal'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/crear/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/<int:paciente_id>/', views.detalles_paciente, name='detalles_paciente'),
    path('pacientes/<int:paciente_id>/editar/', views.editar_paciente, name='editar_paciente'), 
    path('consulta/eliminar/<int:consulta_id>/', views.eliminar_consulta, name='eliminar_consulta'),
    path('paciente/<int:paciente_id>/agregar_consulta/', agregar_consulta, name='agregar_consulta'),
]
