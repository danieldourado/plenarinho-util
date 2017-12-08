from django import forms
from .models import Falas


class FalasForm(forms.ModelForm):
    class Meta:
        model = Falas
        fields = ['name', ]
