from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , DetailView, CreateView , TemplateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.safestring import mark_safe
from .models import Dietas
from .forms import DietaForm
from applications.users.views import AdminRequiredMixin , AlumnoRequiredMixin
from applications.users.models import User
# Create your views here.
###############alumno

class VerAlumnoDieta(AlumnoRequiredMixin, ListView):
    template_name = 'alumno/dieta_alumno.html'
    context_object_name = 'dieta_alumno_por_id'
    model = Dietas
    
    


########################################################################
class ListadietasAdmint(AdminRequiredMixin,ListView):
    template_name = 'administrador/dietas/lista_dietas_admin.html'
    paginate_by = 5
    context_object_name = 'lista_dietas_admin'
    """ model = rutina """
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        # Utilizar Q para combinar condiciones de búsqueda en varios campos
        lista = Dietas.objects.filter(
           Q(fecha__icontains=palabra_clave) |
           Q(nombre__icontains=palabra_clave)
        ).order_by('-fecha')
        return lista

class DietasCreateView(AdminRequiredMixin,CreateView):
    model = Dietas
    template_name = "administrador/dietas/agregar_dietas.html"
    form_class = DietaForm
    success_url = reverse_lazy('dietas_app:listardietasadmin')
 ##########################################################################
    # SOBREESCRIBIENDO EL METODO GET_FORM PARA FILTAR POR IS_USER A LOS ALUMNOS
    def get_form(self, form_class=None):
        form = super(DietasCreateView, self).get_form(form_class)
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
        return super(DietasCreateView, self).form_valid(form)

    
class DietasUpdateView(AdminRequiredMixin, UpdateView):
    model = Dietas
    template_name = "administrador/dietas/editar_dietas.html"
    form_class = DietaForm
   
    success_url = reverse_lazy('dietas_app:listardietasadmin')
 ##########################################################################
    # SOBREESCRIBIENDO EL METODO GET_FORM PARA FILTAR POR IS_USER A LOS ALUMNOS
    def get_form(self, form_class=None):
        form = super(DietasUpdateView, self).get_form(form_class)
        form.fields['alumno'].queryset = User.objects.filter(is_user=True)
        return form
    ##########################################################################
    def get(self, request, *args, **kwargs):
            # Obtén la instancia de la rutina que deseas editar
            self.object = self.get_object()
            # Desactiva el autoescape para el campo ejercicios
            self.object.resumen = mark_safe(self.object.resumen)
            return super().get(request, *args, **kwargs)
    def form_valid(self, form):
        #logica del proceso
        print('*** Metodo post form valid')
        return super(DietasUpdateView, self).form_valid(form)

class DietaDeleteView(AdminRequiredMixin, DeleteView):
    model = Dietas
    template_name = "administrador/dietas/eliminar_dietas.html"

    success_url = reverse_lazy('dietas_app:listardietasadmin')

