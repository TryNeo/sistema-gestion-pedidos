from django.db import models
from apps.acts.models import User
from apps.dbd.modelos.estructura_model_catalogo import Categoria


class Producto(models.Model):
    id_producto = models.AutoField(primary_key = True)
    nombre = models.CharField("Nombre",max_length=150,unique=True)
    descripcion =  models.TextField("Descripcion",max_length=250,blank=True, null=True)
    imagen = models.ImageField(upload_to="product/%Y/%m/%d",blank=True, null=True)
    costo = models.DecimalField('Costo',default=0.00, max_digits=9, decimal_places=2)
    precio =  models.DecimalField('Precio',default=0.00, max_digits=9, decimal_places=2)
    id_categoria = models.ForeignKey(Categoria, related_name='fk_categoria', on_delete=models.CASCADE)
    estado = models.BooleanField("Activo/Inactivo",default=True)
    fecha_crea = models.DateField("Fecha Creacion",auto_now_add=True)
    fecha_modifica = models.DateField("Fecha Modificacion", auto_now=True)
    usuario_crea =  models.ForeignKey(User,on_delete=models.CASCADE)
    usuario_modifica = models.ForeignKey(User,related_name="fk_usuario_four",blank=True, null=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id_producto']
    
    def __str__(self):
        return '{}'.format(self.nombre)