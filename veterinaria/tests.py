from django.test import TestCase
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
