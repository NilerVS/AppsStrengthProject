from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegisterForm, LoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
# Create your views here.
from django.db.models import Q
from django.views.generic import View,ListView , DetailView, CreateView , TemplateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.utils import timezone
from datetime import datetime, timedelta,date
from applications.clases.models import Clases
#from applications.dietas.models import Dietas 
from django.views.generic.edit import (
    FormView
)

from .models import User
####################################################################################
#mixin

class NotAccessTemplate(TemplateView):
    template_name = 'NotAccess.html'

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff
    def handle_no_permission(self):
        # Redireccionar a la página de denegación de acceso para administradores
        return redirect('users_app:notaccess')


class AlumnoRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and not (self.request.user.is_staff or self.request.user.is_admin)
    
    def handle_no_permission(self):
        # Redireccionar a la página de denegación de acceso para administradores
        return redirect('users_app:notaccess')

####################################################################################

####################################################################################
#PAra vista usuario


class InicioView(TemplateView):
    """vist que carga la pagina de inicio"""
    template_name = 'inicio.html'

class ConocecoachView(TemplateView):
    """vist que carga la pagina de inicio"""
    template_name = 'conocecoach.html'

class DiapruebaView(TemplateView):
    """vist que carga la pagina de inicio"""
    template_name = 'diaprueba.html'
class AlumnosinfoView(TemplateView):
    """vist que carga la pagina de inicio"""
    template_name = 'alumnosinfo.html'

class HorariosclasesinfoView(TemplateView):
    """vist que carga la pagina de inicio"""
    template_name = 'horariosclaseinfo.html'
class PlanesinfoView(TemplateView):
    """vist que carga la pagina de inicio"""
    template_name = 'planesinfo.html'
class CompetenciasinfoView(TemplateView):
    """vist que carga la pagina de inicio"""
    template_name = 'competenciasinfo.html'




class ListAllalumnos(ListView):
    template_name = 'alumnosinfo.html'
    #paginate_by = 4
    #ordering= 'apellido'
    context_object_name = 'lista_alumnos'
    
    model = User
   
    def get_queryset(self):
            # Filtrar solo los usuarios que son is_user
            queryset = User.objects.filter(is_user=True)
            return queryset
####################################################################################

class LoginUser(FormView):
    template_name= 'login.html'
    form_class= LoginForm
    #success_url = reverse_lazy('alumno_app:inicio')
    def form_valid(self, form): 
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        if user:
            login(self.request, user)

            if user.is_staff or user.is_admin:
                # Redirigir a las vistas de admin
                return redirect('users_app:listaralumnosadmin')
            elif user.is_user:
                # Redirigir al usuario normal a la vista de resumenalumno
                return redirect('users_app:resumenalumno', pk=user.pk)

        return super().form_valid(form)
    
class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(reverse('users_app:inicio'))

#############################################################
#POCO:Desde aqui todo lo relacionado con vistas para alumno
#############################################################
class ListByAlumno(AlumnoRequiredMixin, DetailView):
    template_name = 'alumno/resumen.html'
    #login_url = reverse_lazy('users_app:resumenalumno')
    context_object_name = 'listar_alumno_por_id'
    model = User
  
    def get_context_data(self, **kwargs):
        context = super(ListByAlumno, self).get_context_data(**kwargs)
        return context
    
class ListAlumnoClases(AlumnoRequiredMixin, DetailView):
    template_name = 'alumno/dias_clase_alumno.html'
    context_object_name = 'datos_alumno_clase_por_id'
    model = User
  
    def get_context_data(self, **kwargs):
        context = super(ListAlumnoClases, self).get_context_data(**kwargs)
        ###########################################################################
         # Calcular inicio y fin de la semana
        today = timezone.now().date()
        inicio_semana = today - timedelta(days=today.weekday())
        fin_semana = inicio_semana + timedelta(days=6)

        # Filtrar clases por fecha
        clases_semana = Clases.objects.filter(
            alumno=self.object,
            fecha__range=[inicio_semana, fin_semana]
        ).order_by('fecha')
     
    
        context['inicio_semana'] = inicio_semana
        context['fin_semana'] = fin_semana
        context['clases_semana'] = clases_semana
      
        # Identificar el índice de la clase cercana en la lista
       

        ############################################################################
        return context


#############################################################
#POCO:Desde aqui todo lo relacionado con vistas para admin
#############################################################


class ListaalumnosAdmint(AdminRequiredMixin, ListView):
    template_name = 'administrador/alumnos/lista_alumnos_admin.html'
    #login_url = reverse_lazy('users_app:loginruser')
    paginate_by = 5
    ordering= 'apellido'
    context_object_name = 'lista_alumnos_admin'
    #model = User

    """ def get_context_data(self, **kwargs):
        context = super(ListaalumnosAdmint, self).get_context_data(**kwargs)
        return context """
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        
        # Utilizar Q para combinar condiciones de búsqueda en varios campos
        lista = User.objects.filter(
            Q(nombres__icontains=palabra_clave) |
            Q(apellidos__icontains=palabra_clave) |
            Q(edad__icontains=palabra_clave) |
            Q(talla__icontains=palabra_clave) |
            Q(celular__icontains=palabra_clave) |
            Q(celular2__icontains=palabra_clave) |
            Q(direccion__icontains=palabra_clave) |
            Q(redsocial__icontains=palabra_clave),
            is_user=True  # Solo usuarios con is_user=True
        ).order_by('apellidos')

        return lista
class UserRegisterView(AdminRequiredMixin,FormView):
    template_name= 'administrador/alumnos/agregar_alumno.html'
    form_class= UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            edad=form.cleaned_data['edad'],
            talla=form.cleaned_data['talla'],
            celular=form.cleaned_data['celular'],
            celular2=form.cleaned_data['celular2'],
            direccion=form.cleaned_data['direccion'],
            redsocial=form.cleaned_data['redsocial'],
            plan=form.cleaned_data['plan'],
        )
        return super(UserRegisterView,self).form_valid(form)
    
""" class AlumnoCreateView(AdminRequiredMixin, CreateView):
    model = User
    template_name = "administrador/alumnos/agregar_alumno.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:listaralumnosadmin')

    def form_valid(self, form):
        #logica del proceso
        alumno = form.save(commit=False)
        alumno.full_name = alumno.nombres + ' ' + alumno.apellidos
        alumno.save()
        return super(AlumnoCreateView, self).form_valid(form)
     """
class AlumnoUpdateView(AdminRequiredMixin,UpdateView):
    model = User
    template_name = "administrador/alumnos/editar_alumno.html"
    #form_class = UserRegisterForm
    fields = [
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

        ]
    success_url = reverse_lazy('users_app:listaralumnosadmin')

   
    def form_valid(self, form):
        #logica del proceso
        print('*** Metodo post form valid')
        return super(AlumnoUpdateView, self).form_valid(form)
    
class AlumnoDeleteView(AdminRequiredMixin,DeleteView):
    model = User
    template_name = "administrador/alumnos/eliminar_alumno.html"

    success_url = reverse_lazy('users_app:listaralumnosadmin')
