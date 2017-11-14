from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, 'portal/home.html', {})


def contato(request):
    return render(request, 'portal/contato.html', {})


@login_required
def sobre(request):
    return render(request, 'portal/sobre.html', {})
