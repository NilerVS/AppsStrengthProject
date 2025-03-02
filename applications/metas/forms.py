from django import forms
from django.forms import Textarea
from .models import Metas

from django.core.validators import MinValueValidator
class MetasForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Metas
        fields = (
            'nombre',
           
            'alumno',
            'peso',
            'pr',
            )
        widgets = {
            'nombre': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'alumno': forms.Select(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'title': 'Ingresa Peso', 'placeholder': 'Ingresa el peso actual del alumno'}),
            'pr': forms.NumberInput(attrs={'class': 'form-control', 'title': 'Ingresa PR', 'placeholder': 'Ingresa PR'}),
        }
        validators = {
            'pr': [MinValueValidator(0, message='El PR debe ser un número entero positivo.')]
        }