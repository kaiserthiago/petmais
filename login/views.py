from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.urls import reverse

# Create your views here.
from login.forms import RegistroForm


def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'].lower(),
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )
            login(request, new_user)
            return redirect('home')
    else:
        form = RegistroForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)



def register_success(request):
    return render_to_response('registration/success.html', {})
