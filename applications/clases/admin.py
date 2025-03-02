from django.contrib import admin

# Register your models here.
from .models import Clases, Rutina
# Register your models here.

class claseAdmin(admin.ModelAdmin):
    list_display =(
        'id',
        'nombre',
        'fecha',

       

    )


admin.site.register(Clases, claseAdmin)
admin.site.register(Rutina)