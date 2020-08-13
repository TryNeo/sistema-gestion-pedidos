from django import forms 
from apps.dbd.modelos.estructura_model_proveedor import *

class ProveedorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control'
                }
            )

    class Meta:
        model = Proveedor
        fields = [
            'nombre',
            'ruc',
            'descripcion',
            'correo',
            'telefono',
            'direccion',
            'codigo_postal',
            'pais',
            'provincia',
            'ciudad',
            'estado']

        labels = {
            'nombre':'Proveedor:',
            'ruc': 'RUC:',
            'descripcion':'Descripcion:',
            'correo':'Correo Electronico:',
            'telefono':'Telefono:',
            'direccion':'Direccion:',
            'codigo_postal':'Codigo Postal:',
            'pais':'Pais:',
            'provincia':'Provincia:',
            'ciudad':'Ciudad:',
            'estado':"Estado:"
        }

        
        widget={
            'descripcion':forms.Textarea(
                attrs={
                    'rows': 3,
                }
            ),
        }