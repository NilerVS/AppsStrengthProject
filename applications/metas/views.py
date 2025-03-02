from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , DetailView, CreateView , TemplateView, UpdateView, DeleteView
from django.db.models import Q
# Create your views here.
from .forms import MetasForm
from .models import Metas
from applications.users.views import AdminRequiredMixin, AlumnoRequiredMixin
from applications.users.models import User


###############alumno

class VerAlumnoMetas(AlumnoRequiredMixin, ListView):
    template_name = 'alumno/metas_alumno.html'
    context_object_name = 'metas_alumno_por_id'
    model = Metas
    ordering = ['-fecha']
    


##########################################################################################

class ListAllMetas(AdminRequiredMixin, ListView):
    template_name = 'alumnosinfo.html'
    #paginate_by = 4
    #ordering= 'apellido'
    context_object_name = 'lista_metas'
    model = Metas

class ListametassAdmint(AdminRequiredMixin, ListView):
    template_name = 'administrador/metas/lista_metas_admin.html'
    paginate_by = 5
    context_object_name = 'lista_metas_admin'
    """ model = rutina """
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        # Utilizar Q para combinar condiciones de búsqueda en varios campos
        lista = Metas.objects.filter(
           Q(fecha__icontains=palabra_clave) |
           Q(nombre__icontains=palabra_clave)
        ).order_by('-fecha')
        return lista
class MetasCreateView(AdminRequiredMixin, CreateView):
    model = Metas
    template_name = "administrador/metas/agregar_metas.html"
    form_class = MetasForm
    success_url = reverse_lazy('metas_app:listarmetasadmin')
 ##########################################################################
    # SOBREESCRIBIENDO EL METODO GET_FORM PARA FILTAR POR IS_USER A LOS ALUMNOS
    def get_form(self, form_class=None):
        form = super(MetasCreateView, self).get_form(form_class)
        form.fields['alumno'].queryset = User.objects.filter(is_user=True)
        return form
    ##########################################################################
    def form_valid(self, form):
        # Obtén la instancia del alumno seleccionado y asígnala al formulario
        alumno = form.cleaned_data['alumno']
        form.instance.alumno = alumno

        #logica del proceso
        meta = form.save(commit=False)
        """ rutina.full_name = Rutina.nombre + ' ' + rutina.apellido """
        meta.save()
        return super(MetasCreateView, self).form_valid(form)

class MetasUpdateView(AdminRequiredMixin, UpdateView):
    model = Metas
    template_name = "administrador/metas/editar_metas.html"
    form_class = MetasForm
   
    success_url = reverse_lazy('metas_app:listarmetasadmin')
 ##########################################################################
    # SOBREESCRIBIENDO EL METODO GET_FORM PARA FILTAR POR IS_USER A LOS ALUMNOS
    def get_form(self, form_class=None):
        form = super(MetasUpdateView, self).get_form(form_class)
        form.fields['alumno'].queryset = User.objects.filter(is_user=True)
        return form
    ##########################################################################
    def form_valid(self, form):
        #logica del proceso
        print('*** Metodo post form valid')
        return super(MetasUpdateView, self).form_valid(form)
