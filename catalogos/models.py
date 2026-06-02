from django.db import models

# 1. Primero los modelos que no dependen de nadie
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, default="N/A") # <--- TE FALTABA ESTE
    direccion = models.TextField()
    imagen = models.ImageField(upload_to='sucursales/', blank=True, null=True)
    ubicacion_mapa = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

    def __str__(self):
        return self.nombre

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre

# 2. Ahora los modelos que dependen de los anteriores
class Vendedor(models.Model):
    nombre = models.CharField(max_length=150)
    # Como Sucursal ya se definió arriba, esto funcionará
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True, null=True, blank=True) # Permite nulos para el proceso de carga
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0) # Valor por defecto
    status = models.CharField(max_length=20, default='Activo')