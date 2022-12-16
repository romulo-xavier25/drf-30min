from django import forms
from core.models import Contato


class ContatoForm(forms.ModelForm):
    
    class Meta:
        model = Contato
        fields = ('name', 'email', 'phone', 'subject', 'message')
       