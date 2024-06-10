from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    """Представлення домашньої сторінки"""
    return render(request, 'main/home.html')


def contact(request):
    """Представлення сторінки контактів"""
    return render(request, 'main/contact.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})
