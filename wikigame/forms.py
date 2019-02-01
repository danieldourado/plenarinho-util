from django import forms
from .models import WikiGame


class WikiGameForm(forms.ModelForm):
    class Meta:
        model = WikiGame
        fields = ['name', ]
