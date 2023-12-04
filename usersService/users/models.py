from django.db import models

OPCIONES_GENERO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

class Paciente(models.Model):
    cedula = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(choices=OPCIONES_GENERO, max_length=2)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"Paciente: {self.nombre} - Cédula: {self.cedula}"

class Doctor(models.Model):
    cedula = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"Dr. {self.nombre} - Cédula: {self.cedula}"