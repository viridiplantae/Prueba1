from django.db import models

# Create your models here.
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)

class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey(
        Marca, on_delete=models.CASCADE
    )
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Inventario(models.Model):
    codigo = models.ForeignKey(
        Auto, on_delete=models.CASCADE
    )
    descripcion = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ventas(models.Model):
    cod_inventario = models.ForeignKey(
        Inventario, on_delete=models.CASCADE, null=True
        )
    cantidad_venta = models.PositiveIntegerField(null=True)
    venta_valida = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)