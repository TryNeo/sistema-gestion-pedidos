from django import forms 
from apps.dbd.modelos.esctructura_model_cliente import Cliente


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control'
                }
            )

    
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','cedula','correo','telefono','direccion']
        labels = {
            'nombre':'Nombre:',
            'apellido':'Apellido:',
            'cedula':'Cedula:',
            'correo':'Correo:',
            'telefono':'Telefono:',
            'direccion':'Direccion:'
        }