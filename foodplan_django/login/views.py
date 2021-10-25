# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm


def login(request):
    context = {
        'name': 'Foodplan'
    }
    return render(request, 'login/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {
        'name': 'Foodplan',
        'form': form
    }
    return render(request, 'login/register.html', context)