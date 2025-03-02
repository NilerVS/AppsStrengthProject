from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from applications.users.models import User
class Dietas(models.Model):

    alumno = models.ForeignKey(User, on_delete=models.CASCADE,blank = True, null=True)

    nombre = models.CharField('nombre_dieta', max_length=50, blank = True, null=True)
    fecha = models.DateField('fecha_dieta', auto_now=False, auto_now_add=True, blank = True, null=True)
    resumen = RichTextField(blank = True, null=True)


    resumen = RichTextField(blank = True, null=True)


    def __str__(self):
        return str(self.id) + '-' + self.nombre + '-' + str(self.fecha)