import re
from django import forms
from .models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введіть пароль'
        })
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Повторіть пароль'
        })
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: Ivan'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: Petrov'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ex: example@example.com'}),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ex: +380671234567',
                'pattern': r'^\+?\d{9,15}$',
                'title': 'Введіть номер у форматі: +380123456789'
            }),
        }
        help_texts = {
            'phone_number': 'Введіть номер у форматі: +380671234567',
            'username': 'До 150 символів. Лише літери, цифри та @/./+/-/_.',
        }
        error_messages = {
            'email': {
                'invalid': 'Введіть коректну адресу електронної пошти.',
            }
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^\+380\d{9}$', phone_number):
            raise forms.ValidationError('Введіть коректний номер телефону.')
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError('Введіть коректну адресу електронної пошти.')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.match(r'^[A-Za-z]+$', first_name.capitalize()):
            raise forms.ValidationError('Некоректний формат імені.')
        return first_name.capitalize()

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match(r'^[A-Za-z]+$', last_name.capitalize()):
            raise forms.ValidationError('Некоректний формат прізвища.')
        return last_name.capitalize()

