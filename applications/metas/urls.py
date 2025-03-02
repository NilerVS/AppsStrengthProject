from django.urls import path
from . import views

app_name="metas_app"

urlpatterns = [
    path('listar-metas/', views.ListametassAdmint.as_view(), name = 'listarmetasadmin'),
    path('crear-metas/', views.MetasCreateView.as_view(), name = 'crearmetasadmin'),
    path('editar-metas/<pk>/', views.MetasUpdateView.as_view(), name = 'editarmetasadmin'),

    #Alumnos
    path('metas-alumno/<pk>/', views.VerAlumnoMetas.as_view(), name = 'vermetasalumnos'), 
]