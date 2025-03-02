from django import forms
from django.forms import Textarea
from .models import Dietas

from applications.users.models import User
class DietaForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Dietas
        fields = (
            'nombre',
            'resumen',
            'alumno',
            )
        
        widgets = {    
                'nombre': forms.TextInput(attrs={'class': 'form-control',"title": "Ingresa Nombre", 'placeholder': 'Ingresa Nombre de la dieta'}),
                'resumen': Textarea(attrs={'class': 'form-control', "title": "Ingresa Resumen", 'placeholder': 'Resumen'}),
                'alumno': forms.Select(attrs={'class': 'form-control'}),
            }