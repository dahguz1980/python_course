from django.db import models

from cliente.models import Cliente


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre + " " + str(self.precio)


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return (
            self.cliente.nombre + " " + self.producto.nombre + " " + str(self.cantidad)
        )
