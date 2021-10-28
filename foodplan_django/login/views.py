from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import UserRegisterForm

_app_name = 'Foodplan'


def login(request):
    context = {
        'name': _app_name
    }
    return render(request, 'login/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {
        'name': _app_name,
        'form': form
    }
    return render(request, 'login/register.html', context)
