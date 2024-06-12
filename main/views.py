from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm

def home(request):
    """Представлення домашньої сторінки"""
    return render(request, 'main/home.html')


def contact(request):
    """Представлення сторінки контактів"""
    return render(request, 'main/contact.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # Автоматичний вхід користувача після реєстрації
            user = authenticate(username=new_user.username, password=form.cleaned_data['password'])
            login(request, user)
            return redirect('home')  # Замість 'home' можна вказати іншу назву URL
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})
