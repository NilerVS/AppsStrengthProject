from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
from applications.users.models import User

class Metas(models.Model):
    
    NOMBRE_CHOICES= (
        ('0', 'Press banca'),
        ('1', 'Sentadilla'),
        ('2', 'Peso muerto'),
        ('3', 'Fondos'),
        ('4', 'Pull ups'),
        ('5', 'Chin ups'),
    )
     
    alumno = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null=True)

    nombre = models.CharField('nombre_meta', max_length=2, choices=NOMBRE_CHOICES,blank = True, null=True)
    
    fecha = models.DateField('fecha_meta', auto_now=False, auto_now_add=True)
    pr = models.DecimalField('PR', max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    peso = models.DecimalField('Peso', max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])


    def __str__(self):
        return str(self.id) + '-' + str(self.nombre)