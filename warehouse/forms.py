from django import forms
from .models import Products

class ProductForm(forms.ModelForm):

    class Meta:
        model=Products
        fields= ['name', 'warehouse']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'warehouse': forms.Select(attrs={'class': 'form-control'}),
        }
