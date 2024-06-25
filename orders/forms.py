from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'phone_number']

    address = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Адреса доставки'}))
    phone_number = forms.CharField(max_length=13, required=True, widget=forms.TextInput(attrs={'placeholder': 'Контактний телефон'}))
