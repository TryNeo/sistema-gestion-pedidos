from django import forms 
from apps.dbd.modelos.estructura_model_producto import Producto #importamos nuestro model Producto

#Creamos ProductoForm
class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): #sobreescribimos el metodo constructor
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):#realizamos un iteracion a nuestros fields 
            self.fields[field].widget.attrs.update(#y actualizamos para que todos tenga la misama clase
                {
                    'class':'form-control'
                }
            )
        self.fields['id_categoria'].empty_label = "Selecione categoria" #le pones un nombre al label de nuestro select que por defecto tendria un -----------

    class Meta:
        model = Producto #Pasamos nuestro model
        fields = ['nombre','descripcion','imagen','costo','id_categoria','estado','existencia'] #le pasamos los fields en una lista los cuales vamos a estar utilizando
        labels = {#le agregamos un label(etiqueta)
            'nombre':'Producto:',
            'descripcion':'Descripcion:',
            'imagen':'imagen',
            'costo':'Costo:',
            'id_categoria':'Categoria:',
            'estado':'Estado:',
            'existencia':'Existencia:'
        }

    #sobreescribmos el metodo clean
    def clean(self):
        try:#hacemos uso de un try execept
            pro = Producto.objects.get(
                    nombre = self.cleaned_data["nombre"] #obtenemos la data de nuesto form
                )
            if not self.instance.pk: #comprobamos nuesto pk, esto aplica si ya existe
                raise forms.ValidationError("Registro ya existente")
            elif self.instance.pk != pro.pk: #vemos si el pk es diferecial , esto aplica cuando es edicion
                raise forms.ValidationError("Cambio no Permitido , Ya coincide con otro registro")
        except Producto.DoesNotExist: #caso contrario de que no exista simplente lo guardaremos
            pass 
        return self.cleaned_data  #retornamos