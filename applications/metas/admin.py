from django.contrib import admin

# Register your models here.
from .models import Metas
# Register your models here.

class MetasAdmin(admin.ModelAdmin):
    list_display =(
        'alumno',
        'nombre',
        'fecha',
        'pr',
        'peso',
    )

admin.site.register(Metas,MetasAdmin)