from django import forms 
from apps.dbd.modelos.estructura_model_catalogo import Categoria


class CategoriaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control'
                }
            )

    class Meta:
        model = Categoria
        fields = ['nombre','descripcion','estado']
        labels = {
            'nombre':'Categoria:',
            'descripcion':'Descripcion:',
            'estado':"Estado:"
        }

        
        widget={
            'descripcion':forms.Textarea(
                attrs={
                    'rows': 3,
                }
            ),
        }