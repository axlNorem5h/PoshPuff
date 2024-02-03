from django import forms
from django.forms import inlineformset_factory
from .models import Product, Price


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['price', 'currency']


ProductPriceFormSet = inlineformset_factory(Product, Price, form=PriceForm, extra=1)
