from django.db import models

# Create your models here.

class Tipo (models.Model):
    id_tipo  = models.AutoField(db_column='idTipo', primary_key=True) 
    tipo     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipo)

class Provedor(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_tipo          = models.ForeignKey('Tipo',on_delete=models.CASCADE, db_column='idTipo')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)

