from django import forms
from django.forms import Textarea
from .models import Rutina
from .models import Clases
from applications.users.models import User
class RutinaForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Rutina
        fields = (
            'nombre',
            'ejercicios',
            )
        widgets = {    
                'nombre': forms.TextInput(attrs={'class': 'form-control',"title": "Ingresa Nombre", 'placeholder': 'Ingresa Nombre de rutina'}),
                'ejercicios': Textarea(attrs={'class': 'form-control', "title": "Ingresa ejercicios", 'placeholder': 'Bloc'}),
              
            }
        
class ClaseForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Clases
        fields = (
            'nombre',
            'fecha',
            'hora',
            'alumno',
            'rutina',
            )
        alumno = forms.ModelChoiceField(
        queryset=User.objects.all())
    
        widgets = {    
                'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'fecha': forms.DateInput(attrs={'class': 'form-control', 'title': 'Ingresa fecha', 'placeholder': 'Fecha de la clase'}),
                'hora': forms.TimeInput(attrs={'class': 'form-control', 'title': 'Ingresa hora', 'placeholder': 'hora de la clase'}),
                'alumno': forms.Select(attrs={'class': 'form-control'}),
                'rutina': forms.Select(attrs={'class': 'form-control'}),
            }