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
        fields = ['nombre','apellido','cedula','correo','telefono','direccion','estado']
        labels = {
            'nombre':'Nombre:',
            'apellido':'Apellido:',
            'cedula':'Cedula:',
            'correo':'Correo:',
            'telefono':'Telefono:',
            'direccion':'Direccion:',
            'estado':'Estado:'
        }

    def clean(self):
        try:
            super(ClienteForm,self).clean()
            cli = Cliente.objects.get(
                    nombre = self.cleaned_data["nombre"]
                )
            if not self.instance.pk:
                raise forms.ValidationError("Registro ya existente")
            elif self.instance.pk != cli.pk:
                raise forms.ValidationError("Cambio no Permitido , Ya coincide con otro registro")
        except Cliente.DoesNotExist:
            pass
        return self.cleaned_data 