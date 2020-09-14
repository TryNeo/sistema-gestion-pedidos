from django import forms 
from django.contrib.auth.models import Group


class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control'
                }
            )

    class Meta:
        model = Group
        fields = ['name','permissions']
        labels = {
            'nombre':'name',
            'permisos':'permissions',
        }

    def clean(self):
        try:
            grou = Group.objects.get(
                    name = self.cleaned_data["name"]
                )
            if not self.instance.pk:
                raise forms.ValidationError("Registro ya existente")
            elif self.instance.pk != grou.pk:
                raise forms.ValidationError("Cambio no Permitido , Ya coincide con otro registro")
        except Group.DoesNotExist:
            pass
        return self.cleaned_data 