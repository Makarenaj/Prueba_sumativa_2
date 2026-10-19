from django.contrib import admin
from .models import Atencion, Cliente


class AtencionInline(admin.TabularInline):
    model = Atencion
    extra = 0


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "rut", "telefono", "monto")
    search_fields = ("nombre", "rut", "telefono")
    inlines = (AtencionInline,)


@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "cliente", "fecha", "monto")
    list_filter = ("fecha",)
    search_fields = ("titulo", "cliente__nombre", "descripcion")
