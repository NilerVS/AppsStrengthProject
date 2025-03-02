from django.urls import path
from . import views

app_name="users_app"


urlpatterns = [
    #path('registrar/', views.UserRegisterView.as_view(), name = 'registraruser'),

    #""" Para vista de cliente """

    path('', views.InicioView.as_view(), name= 'inicio'),
    path('conoce-coach/', views.ConocecoachView.as_view(), name = 'conocecoachinfo'),
    path('dia-prueba/', views.DiapruebaView.as_view(), name = 'diapruebainfo'),
    path('alumnos-info/', views.ListAllalumnos.as_view(), name = 'alumnosinfo'),
    path('horarios-clases/', views.HorariosclasesinfoView.as_view(), name = 'horarioclaseinfo'),
    path('planes/', views.PlanesinfoView.as_view(), name = 'planesinfo'),
    path('competencias/', views.CompetenciasinfoView.as_view(), name = 'competenciainfo'),

    #""" Para logear o salir """
    path('login/', views.LoginUser.as_view(), name = 'loginruser'),
    path('logout/', views.LogoutView.as_view(), name = 'logoutuser'),


    path('notaccess/', views.NotAccessTemplate.as_view(), name = 'notaccess'),
    #""" alumno """

    path('resumen-alumno/<pk>', views.ListByAlumno.as_view(), name = 'resumenalumno'),
    path('clase-alumno/<pk>', views.ListAlumnoClases.as_view(), name = 'clasealumnoporid'), 
   


    #""" administrador """
    path('listar-alumnos/', views.ListaalumnosAdmint.as_view(), name = 'listaralumnosadmin'),
    path('registrar/', views.UserRegisterView.as_view(), name = 'agregaralumnosadmin'),
    #path('agregar-alumnos/', views.AlumnoCreateView.as_view(), name = 'agregaralumnosadmin'),  
    path('editar-alumnos/<pk>/', views.AlumnoUpdateView.as_view(), name = 'editaralumnosadmin'),
    path('eliminar-alumnos/<pk>/', views.AlumnoDeleteView.as_view(), name = 'eliminaralumnosadmin'),
]