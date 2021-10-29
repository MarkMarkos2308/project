from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, Contact_us
import time


def home(request):
    return render(request, 'myfirstapp/home.html')


def singup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'myfirstapp/singup.html', {'form': form})


@login_required
def user_profile(request):
    return render(request, 'myfirstapp/uprof.html')


