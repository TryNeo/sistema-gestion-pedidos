from django.db import models
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from apps.acts.models import User
from apps.dbd.modelos.estructura_model_catalogo import Categoria
from apps.dbd.modelos.esctructura_model_cliente import Cliente
from apps.dbd.modelos.estructura_model_producto import Producto
from apps.dbd.choices import ESTADO_CHOICES,PAGO_CHOICES
from django.db.models import Sum
from django.db.models.functions import Coalesce

class Pedido(models.Model):
    id_pedido =  models.AutoField(primary_key = True)
    num_pedido = models.CharField(max_length=100,unique=True)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    nota = models.TextField(max_length=250,blank=True, null=True)
    forma_pago = models.CharField(max_length=50, choices = PAGO_CHOICES, default="Efectivo")
    estado_pedido = models.CharField(max_length=10, choices = ESTADO_CHOICES, default="Pediente")
    fecha_pedido = models.DateField("Fecha de orden")
    subtotal = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)

    estado = models.BooleanField(default=True, verbose_name='Activo/Inactivo')
    fecha_crea = models.DateField(auto_now_add=True, verbose_name='Fecha Creacion')
    fecha_modifica = models.DateField(auto_now=True, verbose_name='Fecha Modificacion')
    usuario_crea = models.ForeignKey(User,on_delete=models.CASCADE)
    usuario_modifica = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='fk_usuario_six')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-num_pedido']

    def __str__(self):
        return '{}'.format(self.num_pedido)
    
    def save(self):
        self.total = self.subtotal + self.iva
        super(Pedido,self).save()



class PedidoItem(models.Model):
    id_pedido_item =  models.AutoField(primary_key = True)
    pedido = models.ForeignKey(Pedido,on_delete = models.CASCADE)
    producto =  models.ForeignKey(Producto,on_delete = models.CASCADE)
    precio =  models.DecimalField('Precio',default=0.00, max_digits=9, decimal_places=2)
    
    cantidad = models.IntegerField(default=0)

    subtotal = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)

    class Meta:
        verbose_name = 'Pedido item'
        verbose_name_plural = 'Pedido items'
        ordering = ['id_pedido_item']

    def __str__(self):
        return '{}'.format(self.id_pedido_item)


    def save(self):
        self.subtotal = float(float(int(self.cantidad)) * float(self.precio))
        self.iva = float(float(int(self.subtotal)))* float(int(self.iva)/100)
        self.total = self.subtotal+self.iva
        super(PedidoItem,self).save()



@receiver(post_delete,sender=PedidoItem)
def pedido_item_bor(sender,instance,**kwargs):
    id_producto = instance.producto.id_producto
    id_pedido = instance.pedido.id_pedido
    
    enc = Pedido.objects.filter(pk=id_pedido).first()
    if enc:
        subtotal = PedidoItem.objects.filter(pedido=id_pedido).aggregate(r=Coalesce(Sum('subtotal'),0)).get('r')
        iva =PedidoItem.objects.filter(pedido=id_pedido).aggregate(r=Coalesce(Sum('iva'),0)).get('r')
        enc.subtotal = float(subtotal)
        enc.iva=float(iva)
        enc.save()

    prod = Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) + int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()

@receiver(post_save,sender=PedidoItem)
def pedido_item_sav(sender,instance,**kwargs):
    id_producto = instance.producto.id_producto
    prod = Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) - int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()