from django.db import models
from apps.acts.models import User


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre",max_length=50)
    apellido = models.CharField("Apellido",max_length=50)
    cedula = models.CharField("Cedula",max_length=10, unique=True)
    correo = models.EmailField("Email",default='example@gmail.com', max_length=254, unique=True)
    telefono = models.CharField("Telefono",blank=True, default='xxx-xxx-xxxx', max_length=10, null=True, unique=True)
    direccion = models.CharField("Direccion",blank=True, max_length=250, null=True)
    estado = models.BooleanField(default=True, verbose_name='Activo/Inactivo')
    fecha_crea = models.DateField(auto_now_add=True, verbose_name='Fecha Creacion')
    fecha_modifica = models.DateField(auto_now=True, verbose_name='Fecha Modificacion')
    usuario_crea = models.ForeignKey(User,on_delete=models.CASCADE)
    usuario_modifica = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='fk_usuario_three')
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id_cliente']

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido)