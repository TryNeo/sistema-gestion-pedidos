from django.db import models
from apps.acts.models import User

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key = True)
    nombre = models.CharField("Nombre",max_length=150,unique=True)
    descripcion = models.TextField("Descripcion",max_length=250)
    estado = models.BooleanField("Activo/Inactivo",default=True)
    fecha_crea = models.DateField("Fecha Creacion",auto_now_add=True)
    fecha_modifica = models.DateField("Fecha Modificacion", auto_now=True)
    usuario_crea =  models.ForeignKey(User,on_delete=models.CASCADE)
    usuario_modifica = models.ForeignKey(User,related_name="fk_usuario",blank=True, null=True,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id_categoria']

    def __str__(self):
        return '{}'.format(self.nombre)