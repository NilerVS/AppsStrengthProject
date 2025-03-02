from django.urls import path
from . import views

app_name="dietas_app"

urlpatterns = [
    path('listar-dietas/', views.ListadietasAdmint.as_view(), name = 'listardietasadmin'),
    path('crear-dietas/', views.DietasCreateView.as_view(), name = 'creardietasadmin'),
    path('editar-dietas/<pk>/', views.DietasUpdateView.as_view(), name = 'editardietasadmin'),
    path('eliminar-dietas/<pk>/', views.DietaDeleteView.as_view(), name = 'eliminardietasadmin'),

    #  Alumnos
    path('dieta-alumno/<pk>', views.VerAlumnoDieta.as_view(), name = 'dietaalumnoporid'),

]