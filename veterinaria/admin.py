from django.contrib import admin
from .models import Atencion, Cliente


def monto_en_pesos(monto):
    return f"${format(monto, ',.0f').replace(',', '.')}"


class AtencionInline(admin.TabularInline):
    model = Atencion
    extra = 0


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "rut", "telefono", "monto_pesos")
    list_filter = ("monto",)
    search_fields = ("nombre", "rut", "telefono")
    inlines = (AtencionInline,)

    @admin.display(description="Monto (CLP)", ordering="monto")
    def monto_pesos(self, obj):
        return monto_en_pesos(obj.monto)


@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "cliente", "fecha", "monto_pesos")
    list_filter = ("fecha", "cliente")
    search_fields = ("titulo", "cliente__nombre", "descripcion")

    @admin.display(description="Monto (CLP)", ordering="monto")
    def monto_pesos(self, obj):
        return monto_en_pesos(obj.monto)
