from django import forms 
from apps.dbd.modelos.estructura_model_producto import Producto

class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control'
                }
            )
        self.fields['id_categoria'].empty_label = "Selecione categoria"

    class Meta:
        model = Producto
        fields = ['nombre','descripcion','imagen','costo','precio','id_categoria']
        labels = {
            'nombre':'Producto:',
            'descripcion':'Apellido:',
            'imagen':'Imagen Producto:',
            'costo':'Costo:',
            'precio':'Precio:',
            'id_categoria':'Categoria:',
            'estado':'Estado:'
        }