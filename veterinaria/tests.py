from decimal import Decimal
from django.contrib import admin
from django.test import RequestFactory, TestCase
from .admin import AtencionAdmin, ClienteAdmin, monto_en_pesos
from .models import Atencion, Cliente


class ClienteAtencionTests(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Ana Pérez",
            rut="12.345.678-9",
            telefono="+56912345678",
            monto="25000.00",
        )
        self.atencion = Atencion.objects.create(
            cliente=self.cliente,
            titulo="Consulta inicial",
            fecha="2026-10-19",
            descripcion="Evaluación general",
            monto="15000.00",
        )

    def test_atencion_queda_asociada_al_cliente(self):
        self.assertEqual(self.atencion.cliente, self.cliente)
        self.assertEqual(self.cliente.atenciones.count(), 1)

    def test_eliminar_cliente_elimina_sus_atenciones(self):
        self.cliente.delete()
        self.assertFalse(Atencion.objects.exists())

    def test_registros_tienen_nombres_legibles(self):
        self.assertEqual(str(self.cliente), "Ana Pérez")
        self.assertEqual(str(self.atencion), "Consulta inicial")

    def test_montos_se_muestran_en_pesos_chilenos(self):
        self.assertEqual(monto_en_pesos(Decimal("12990.00")), "$12.990")
        self.assertEqual(monto_en_pesos(Decimal("1500000.00")), "$1.500.000")

    def test_listados_tienen_columnas_filtros_y_busqueda(self):
        request = RequestFactory().get("/admin/")
        cliente_admin = ClienteAdmin(Cliente, admin.site)
        atencion_admin = AtencionAdmin(Atencion, admin.site)

        self.assertEqual(
            cliente_admin.get_list_display(request),
            ("nombre", "rut", "telefono", "monto_pesos"),
        )
        self.assertTrue(cliente_admin.get_list_filter(request))
        self.assertTrue(cliente_admin.get_search_fields(request))
        self.assertEqual(
            atencion_admin.get_list_display(request),
            ("titulo", "cliente", "fecha", "monto_pesos"),
        )
        self.assertTrue(atencion_admin.get_list_filter(request))
        self.assertTrue(atencion_admin.get_search_fields(request))
