from django.urls import path
from . import views

app_name="rutina_app"

urlpatterns = [
    path('listar-rutinas/', views.ListarutinaAdmint.as_view(), name = 'listarrutinasadmin'),
    path('crear-rutinas/', views.RutinaCreateView.as_view(), name = 'crearrutinasadmin'),
    path('editar-rutinas/<pk>/', views.RutinaUpdateView.as_view(), name = 'editarrutinasadmin'),
    path('eliminar-rutinas/<pk>/', views.RutinaDeleteView.as_view(), name = 'eliminarrutinasadmin'),

    # paths para las clases

    path('listar-clases/', views.ListaclasesAdmint.as_view(), name = 'listaclasesadmin'),
    path('crear-clases/', views.ClaseCreateView.as_view(), name = 'crearclasesadmin'),
    path('editar-clases/<pk>/', views.ClaseUpdateView.as_view(), name = 'editarclasesadmin'),
    path('eliminar-clases/<pk>/', views.ClaseDeleteView.as_view(), name = 'eliminarclasesadmin'),
]   