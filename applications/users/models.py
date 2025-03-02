from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):

    GENDER_CHOISES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    PLAN_CHOICES= (
                ('0', 'Powerlifter'),
                ('1', 'Disminución de grasa'),
                ('2', 'Aumento de peso'),
                ('3', 'Estetico'),
                ('4', 'Calistenia'),
                ('5', 'Personalizado'),
            )
    username = models.CharField(max_length=20, unique=True)
    email= models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=100, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOISES, blank=True)
    edad = models.PositiveIntegerField(null=True, default=0)
    talla = models.DecimalField(max_digits=5, decimal_places=2,default=0.0, help_text='Ingresar talla en metros',blank = True, null=True)
    celular = models.CharField('celular_alumno', max_length=9,blank = True)
    celular2 = models.CharField('celular_alumno2', max_length=9,blank = True)
    direccion = models.CharField('direccion_alumno', max_length=150,blank = True)
    redsocial = models.CharField('red_social', max_length=60,blank = True, null=True)
    fechainicio = models.DateField('fecha_inicio_alumno', auto_now=False,blank = True, auto_now_add=True)
    fechafin = models.DateField('fecha_fin_alumno', auto_now=False, auto_now_add=False, blank = True, null=True)
    plan = models.CharField('plan_alumno', max_length=2, choices=PLAN_CHOICES,blank = True)

    #Administrador de django
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects=UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres+ ' '+self.apellidos