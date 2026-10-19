from django.db import models


class Cliente(models.Model):
    nombre = models.CharField("nombre", max_length=150)
    rut = models.CharField("RUT", max_length=12)
    telefono = models.CharField("teléfono", max_length=20)
    monto = models.DecimalField("monto en pesos", max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ("nombre",)

    def __str__(self):
        return self.nombre


class Atencion(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="atenciones",
        verbose_name="cliente",
    )
    titulo = models.CharField("título", max_length=150)
    fecha = models.DateField("fecha")
    descripcion = models.TextField("descripción")
    monto = models.DecimalField("monto en pesos", max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "atención"
        verbose_name_plural = "atenciones"
        ordering = ("-fecha", "titulo")

    def __str__(self):
        return self.titulo
