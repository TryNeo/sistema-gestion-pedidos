from django import forms 
from apps.dbd.modelos.estructura_model_pedido import Pedido,PedidoItem
from apps.dbd.modelos.esctructura_model_cliente import Cliente


class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset= Cliente.objects.filter(estado=True))
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control'
                }
            )
        self.fields['cliente'].empty_label = "Selecione cliente"
        self.fields['forma_pago'].empty_label = "Selecione forma pago"
        self.fields['estado_pedido'].empty_label = "Selecione estado"
        self.fields['subtotal'].widget.attrs['readonly'] = True
        self.fields['iva'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True
    class Meta:
        model = Pedido
        fields = ['num_pedido','cliente','nota','forma_pago','estado_pedido','fecha_pedido','subtotal','iva','total']


class PedidoCreateForm(forms.ModelForm):   
    cliente = forms.ModelChoiceField(
        queryset= Cliente.objects.filter(estado=True))
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control'
                }
            )
        self.fields['cliente'].empty_label = "Selecione cliente"

    class Meta:
        model = Pedido
        fields = ['num_pedido','cliente']

    def clean(self):
        try:
            ped = Pedido.objects.get(
                    num_pedido = self.cleaned_data["num_pedido"]
                )
            if not self.instance.pk:
                raise forms.ValidationError("Registro ya existente")
            elif self.instance.pk != ped.pk:
                raise forms.ValidationError("Cambio no Permitido , Ya coincide con otro registro")
        except Pedido.DoesNotExist:
            pass
        return self.cleaned_data 

class PedidoEditForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset= Cliente.objects.filter(estado=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control'
                }
            )
        self.fields['cliente'].empty_label = "Selecione cliente"
        self.fields['forma_pago'].empty_label = "Selecione forma pago"
        self.fields['estado_pedido'].empty_label = "Selecione estado"

    class Meta:
        model = Pedido
        fields = ['num_pedido','cliente','nota','forma_pago','estado_pedido']
        exclude = ['subtotal','iva','total','fecha_pedido']
        labels = {
            'num_pedido':'N* Pedido:',
            'nota':'Comentarios o instruciones:',
            'forma_pago':'Forma Pago:',
            'estado_pedido':'Estado Pedido:',
        }

    def clean(self):
        try:
            ped = Pedido.objects.get(
                    num_pedido = self.cleaned_data["num_pedido"]
                )
            if not self.instance.pk:
                raise forms.ValidationError("Registro ya existente")
            elif self.instance.pk != ped.pk:
                raise forms.ValidationError("Cambio no Permitido , Ya coincide con otro registro")
        except Pedido.DoesNotExist:
            pass
        return self.cleaned_data 
