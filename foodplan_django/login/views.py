# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def login(request):
    context = {
        'name': 'Foodplan'
    }
    return render(request, 'login/login.html', context)