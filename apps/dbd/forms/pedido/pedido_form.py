from django import forms 
from apps.dbd.modelos.estructura_model_pedido import Pedido,PedidoItem



class PedidoForm(forms.ModelForm):
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

class PedidoEditForm(forms.ModelForm):
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
            'cliente':'Cliente:',
            'nota':'Comentarios o instruciones:',
            'forma_pago':'Forma Pago:',
            'estado_pedido':'Estado Pedido:',
        }