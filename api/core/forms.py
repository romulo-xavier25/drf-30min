from django import forms
from core.models import Product


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'code', 'value', 'description', 'category')
       