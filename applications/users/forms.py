from django import forms
from django.contrib.auth import authenticate
from .models import User


class UserRegisterForm(forms.ModelForm):
    """Form definition for User."""

    password1= forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder':'contraseña', 'class': 'form-control'})
    )

    password2= forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder':'Repetir contraseña','class': 'form-control'})
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
            'edad',
            'talla',
            'celular',
            'celular2',
            'direccion',
            'redsocial',
            'plan',

        )
        widgets = {    
                'username': forms.TextInput(attrs={'class': 'form-control',"title": "Ingresa Usuario", 'placeholder': 'Ingresa usuario'}),
                'email': forms.TextInput(attrs={'class': 'form-control',"title": "Ingresa Email", 'placeholder': 'Ingresa email'}),
                'nombres': forms.TextInput(attrs={'class': 'form-control',"title": "Ingresa Nombre", 'placeholder': 'Ingresa Nombre'}),
                'apellidos': forms.TextInput(attrs={'class': 'form-control',"title": "Ingresa Apellidos", 'placeholder': 'Ingresa Apellidos'}),
                'genero': forms.Select(attrs={'class': 'form-control'}),
                'edad': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 120, 'placeholder': 'Ingrese Edad'}),
                'talla': forms.TextInput(attrs={ 'class': 'form-control',"title": "Ingresa talla", 'placeholder': 'Ingresa Talla'}),
                'celular': forms.TextInput(attrs={ 'class': 'form-control',"title": "Ingresa celular", 'placeholder': 'Ingresa celular'}),
                'celular2': forms.TextInput(attrs={ 'class': 'form-control',"title": "Ingresa celular respaldo", 'placeholder': 'Celular de respaldo'}),
                'direccion': forms.TextInput(attrs={ 'class': 'form-control',"title": "Ingresa direccion", 'placeholder': 'Ingresa dirección'}),
                'plan': forms.Select(attrs={'class': 'form-control'}),
                'redsocial': forms.TextInput(attrs={'class': 'form-control',"title": "Ingresa red social", 'placeholder': 'Ingresa una red social'}),
            }
    


    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','las contraseñas no coinciden') 

class LoginForm(forms.Form):
    username= forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Ingresa usuario', 'class': 'form-control'})
    )

    password= forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder':'Ingresa contraseña','class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']


        if not authenticate(username=username, password=password):
            raise forms.ValidationError('los datos del usuario no son correctos')
        
        return  self.cleaned_data