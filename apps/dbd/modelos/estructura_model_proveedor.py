from django.db import models
from apps.acts.models import User


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key = True)
    nombre = models.CharField("Nombre",max_length=150,unique=True)
    ruc  =  models.CharField("Ruc",max_length=11,unique=True,blank=True, null=True)
    descripcion = models.TextField("Descripcion",max_length=250, blank=False, null=False)
    correo = models.EmailField("Email",unique=True,blank=False, null=False,default="example@gmail.com")
    telefono = models.CharField("Telefono",max_length=10,unique=True,blank=True, null=True,default="xxx-xxx-xxxx")
    direccion = models.CharField("Nombre",max_length=250,blank=True, null=True)
    codigo_postal = models.CharField("Telefono",max_length=6,blank=False, null=False)
    pais =  models.CharField("Pais",max_length=50,blank=True, null=True)
    provincia = models.CharField("Provincia",max_length=50,blank=True, null=True)
    ciudad =  models.CharField("ciudad",max_length=50,blank=True, null=True)

    estado = models.BooleanField("Activo/Inactivo",default=True)
    fecha_crea = models.DateField("Fecha Creacion",auto_now_add=True)
    fecha_modifica = models.DateField("Fecha Modificacion", auto_now=True)
    usuario_crea =  models.ForeignKey(User,on_delete=models.CASCADE)
    usuario_modifica = models.ForeignKey(User,related_name="fk_usuario_two",blank=True, null=True,on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id_proveedor']
    
    def __str__(self):
        return '{}'.format(self.nombre)