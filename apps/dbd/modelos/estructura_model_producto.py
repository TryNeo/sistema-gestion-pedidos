from django.db import models
from apps.acts.models import User #importando la la aplicacion acts con el modelo User
from apps.dbd.modelos.estructura_model_catalogo import Categoria #importando el modelo de catagalo donde se encuentra categoria
from SistemaGestionPedidos.settings.base import MEDIA_URL,STATIC_URL #importando el static url y el media_url

#Creamos nuestro modelo producto
class Producto(models.Model):
    id_producto = models.AutoField(primary_key = True) 
    nombre = models.CharField("Nombre",max_length=150,unique=True)
    descripcion =  models.TextField("Descripcion",max_length=250,blank=True, null=True)
    imagen = models.ImageField(upload_to="product/%Y/%m/%d",blank=True, null=True)#usamos el ImageField para poder pasarle la url en donde estara ubicando exactamente
    costo = models.DecimalField('Costo',default=0.00, max_digits=9, decimal_places=2)
    existencia  = models.IntegerField(default=0)
    id_categoria = models.ForeignKey(Categoria, related_name='fk_categoria', on_delete=models.CASCADE)#hacemos la relacion de 1 a muchos con categoria
    estado = models.BooleanField("Activo/Inactivo",default=True)
    fecha_crea = models.DateField("Fecha Creacion",auto_now_add=True)
    fecha_modifica = models.DateField("Fecha Modificacion", auto_now=True)
    usuario_crea =  models.ForeignKey(User,on_delete=models.CASCADE)#hacemos la relacion de 1 a muchos con user
    usuario_modifica = models.ForeignKey(User,related_name="fk_usuario_four",blank=True, null=True,on_delete=models.CASCADE)#hacemos la relacion de 1 a muchos con user

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id_producto']
    
    #creamos un metodo get_image para obtener la imagen del 
    def get_image(self):
        if self.imagen:#comprobamos de que dicha imagen existe 
            return '{}{}'.format(MEDIA_URL,self.imagen) #y retornamos con el url la imagen
        return '{}{}'.format(STATIC_URL,'images/empty.png') #caso contrario de que no exista retornamos una imagen por defecto que esta en el static/image
    #obtenemos el nombre del producto
    def __str__(self):
        return '{}'.format(self.nombre)