from django import forms
from .models import Comment, CommentService


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Напишіть ваш коментар...'}),
        }


class CommentServiceForm(forms.ModelForm):
    class Meta:
        model = CommentService
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Напишіть ваш коментар...'}),
        }
