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
            'correo':'Correo:',
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


    def clean(self):
        try:
            prov = Proveedor.objects.get(
                    nombre = self.cleaned_data["nombre"],
                )
            if not self.instance.pk:
                raise forms.ValidationError("Registro ya existente")
            elif self.instance.pk != prov.pk:
                raise forms.ValidationError("Cambio no Permitido , Ya coincide con otro registro")
        except Proveedor.DoesNotExist:
            pass
        return self.cleaned_data 


class ConsultaProveedorForm(forms.ModelForm):
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
            'correo':'Correo:',
            'telefono':'Telefono:',
            'direccion':'Direccion:',
            'codigo_postal':'Codigo Postal:',
            'pais':'Pais:',
            'provincia':'Provincia:',
            'ciudad':'Ciudad:',
            'estado':"Estado:"
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control'
                }
            )
        self.fields['nombre'].widget.attrs['readonly'] = True
        self.fields['ruc'].widget.attrs['readonly'] = True
        self.fields['correo'].widget.attrs['readonly'] = True
        self.fields['telefono'].widget.attrs['readonly'] = True
        self.fields['descripcion'].widget.attrs['readonly'] = True
        self.fields['direccion'].widget.attrs['readonly'] = True
        self.fields['codigo_postal'].widget.attrs['readonly'] = True
        self.fields['pais'].widget.attrs['readonly'] = True
        self.fields['provincia'].widget.attrs['readonly'] = True
        self.fields['ciudad'].widget.attrs['readonly'] = True
        self.fields['estado'].widget.attrs['disabled'] = 'disabled'