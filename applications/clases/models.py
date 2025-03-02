from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
#from applications.alumno.models import Alumno
from applications.users.models import User

class Rutina(models.Model):
     
     nombre = models.CharField('nombre_rutina', max_length=50)

     #dias = models.CharField('dias_clases', max_length=10)
     ejercicios = RichTextField()

     class Meta:
          verbose_name= 'Dia'
          verbose_name_plural = 'rutinas de clases'
    
     def __str__(self):
        return str(self.id) + '-' + self.nombre
    

class Clases(models.Model):
    
    alumno = models.ForeignKey(User, on_delete=models.CASCADE,null=True, max_length=50)

    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    
    nombre = models.CharField('Dia_clase', blank = True, null=True, max_length=50)

    fecha = models.DateField('fecha_clase', auto_now=False, auto_now_add=False)

    hora = models.TimeField('hora_clase', auto_now=False, auto_now_add=False, blank = True, null=True)

    

    def fecha_formateada(self):
        return self.fecha.strftime('%Y-%m-%d')

    def __str__(self):
            return str(self.id) + '-' + str(self.nombre)