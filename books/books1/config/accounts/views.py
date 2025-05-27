from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # автоматический вход после регистрации
            return redirect('home')  # перенаправление после регистрации
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})
