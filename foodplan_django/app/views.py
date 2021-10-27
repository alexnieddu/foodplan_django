from django.shortcuts import render


def home(request):
    context = {
        'name': 'Foodplan'
    }
    return render(request, 'app/home.html', context)
