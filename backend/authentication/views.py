from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CreateUserForm

def home(request):
    return render(request, 'authentication/home.html') 

def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'conta {user} criada com sucesso')
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'authentication/signup.html', {'form':form})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/change-password.html' 
