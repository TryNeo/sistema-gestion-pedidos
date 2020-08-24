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
