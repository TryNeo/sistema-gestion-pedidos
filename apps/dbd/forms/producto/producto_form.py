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
        fields = ['nombre','descripcion','imagen','costo','id_categoria','estado','existencia']
        labels = {
            'nombre':'Producto:',
            'descripcion':'Descripcion:',
            'imagen':'imagen',
            'costo':'Costo:',
            'id_categoria':'Categoria:',
            'estado':'Estado:',
            'existencia':'Existencia:'
        }

    def clean(self):
        try:
            pro = Producto.objects.get(
                    nombre = self.cleaned_data["nombre"]
                )
            if not self.instance.pk:
                raise forms.ValidationError("Registro ya existente")
            elif self.instance.pk != pro.pk:
                raise forms.ValidationError("Cambio no Permitido , Ya coincide con otro registro")
        except Producto.DoesNotExist:
            pass
        return self.cleaned_data 