from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , DetailView, CreateView , TemplateView, UpdateView, DeleteView
from django.db.models import Q
# Create your views here.
from django.utils.safestring import mark_safe
from .forms import RutinaForm
from .forms import ClaseForm
from .models import Rutina
from .models import Clases
from applications.users.views import AdminRequiredMixin
from applications.users.models import User

class ListarutinaAdmint(AdminRequiredMixin,ListView):
    template_name = 'administrador/rutinas/lista_rutina_admin.html'
    
    paginate_by = 5
    ordering= 'nombre'
    context_object_name = 'lista_rutina_admin'
    """ model = rutina """
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        
        # Utilizar Q para combinar condiciones de búsqueda en varios campos
        lista = Rutina.objects.filter(
            nombre__icontains=palabra_clave) 
        return lista
    
class RutinaCreateView(AdminRequiredMixin,CreateView):
    model = Rutina
    template_name = "administrador/rutinas/agregar_rutina.html"
    form_class = RutinaForm
    success_url = reverse_lazy('rutina_app:listarrutinasadmin')

    def form_valid(self, form):
        #logica del proceso
        rutina = form.save(commit=False)
        """ rutina.full_name = Rutina.nombre + ' ' + rutina.apellido """
        rutina.save()
        return super(RutinaCreateView, self).form_valid(form)
    
class RutinaUpdateView(AdminRequiredMixin,UpdateView):
    model = Rutina
    template_name = "administrador/rutinas/editar_rutina.html"
    form_class = RutinaForm
   
    success_url = reverse_lazy('rutina_app:listarrutinasadmin')
    def form_valid(self, form):
        #logica del proceso
        print('*** Metodo post form valid')
        print('Contenido de ejercicios:', form.cleaned_data['ejercicios'])
        return super(RutinaUpdateView, self).form_valid(form)
class RutinaDeleteView(AdminRequiredMixin,DeleteView):
    model = Rutina
    template_name = "administrador/rutinas/eliminar_rutina.html"

    success_url = reverse_lazy('rutina_app:listarrutinasadmin')


#empieza las clases para Clases

class ListaclasesAdmint(AdminRequiredMixin,ListView):
    template_name = 'administrador/clases/lista_clases_admin.html'
    paginate_by = 5
    context_object_name = 'lista_clases_admin'
    """ model = rutina """
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        # Utilizar Q para combinar condiciones de búsqueda en varios campos
        lista = Clases.objects.filter(
           Q(fecha__icontains=palabra_clave)
        ).order_by('-fecha')
        return lista
class ClaseCreateView(AdminRequiredMixin,CreateView):
    model = Clases
    template_name = "administrador/clases/agregar_clases.html"
    form_class = ClaseForm
    success_url = reverse_lazy('rutina_app:listaclasesadmin')
    ##########################################################################
    # SOBREESCRIBIENDO EL METODO GET_FORM PARA FILTAR POR IS_USER A LOS ALUMNOS
    def get_form(self, form_class=None):
        form = super(ClaseCreateView, self).get_form(form_class)
        form.fields['alumno'].queryset = User.objects.filter(is_user=True)
        return form
    ##########################################################################

    def form_valid(self, form):
   # Obtén la instancia del alumno seleccionado y asígnala al formulario
        alumno = form.cleaned_data['alumno']
        form.instance.alumno = alumno

        #logica del proceso
        clase = form.save(commit=False)
        """ rutina.full_name = Rutina.nombre + ' ' + rutina.apellido """
        clase.save()
        return super(ClaseCreateView, self).form_valid(form)
    
class ClaseUpdateView(AdminRequiredMixin,UpdateView):
    model = Clases
    template_name = "administrador/clases/editar_clases.html"
    form_class = ClaseForm
   
    success_url = reverse_lazy('rutina_app:listaclasesadmin')
 ##########################################################################
    # SOBREESCRIBIENDO EL METODO GET_FORM PARA FILTAR POR IS_USER A LOS ALUMNOS
    def get_form(self, form_class=None):
        form = super(ClaseUpdateView, self).get_form(form_class)
        form.fields['alumno'].queryset = User.objects.filter(is_user=True)
        return form
    ##########################################################################
    
    def form_valid(self, form):
        #logica del proceso
        print('*** Metodo post form valid')
        return super(ClaseUpdateView, self).form_valid(form)

class ClaseDeleteView(AdminRequiredMixin,DeleteView):
    model = Clases
    template_name = "administrador/clases/eliminar_clases.html"

    success_url = reverse_lazy('rutina_app:listaclasesadmin')

