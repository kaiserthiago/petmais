from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from portal.forms import PetForm, ContatoForm, EspecieForm, RacaForm
from portal.models import Pet, Contato, Especie, Raca


def home(request):
    pets = Pet.objects.filter(status='Disponível')

    context = {
        'pets': pets,
    }
    return render(request, 'portal/home.html', context)


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)

        if form.is_valid():
            contato = Contato()

            contato.nome = form.cleaned_data['nome']
            contato.email = form.cleaned_data['email']
            contato.comentario = form.cleaned_data['comentario']

            contato.save()

            return redirect('contato')

    form = ContatoForm()
    context = {
        'form': form,
    }
    return render(request, 'portal/contato.html', context)


def sobre(request):
    return render(request, 'portal/sobre.html', {})


@login_required
def especie_new(request):
    if request.method == 'POST':
        form = EspecieForm(request.POST)

        if form.is_valid():
            especie = Especie()

            especie.descricao = form.cleaned_data['descricao']

            especie.save()

            return redirect('my_especies')

    form = EspecieForm()
    context = {
        'form': form,
    }

    return render(request, 'portal/especie_new.html', context)


@login_required
def racas(request):
    racas = Raca.objects.all().order_by('descricao')

    context = {
        'racas': racas,
    }

    return render(request, 'portal/racas.html', context)


@login_required
def raca_new(request):
    if request.method == 'POST':
        form = RacaForm(request.POST)

        if form.is_valid():
            raca = Raca()

            raca.especie = form.cleaned_data['especie']
            raca.descricao = form.cleaned_data['descricao']

            raca.save()

            return redirect('racas')

    form = RacaForm()
    context = {
        'form': form,
    }

    return render(request, 'portal/raca_new.html', context)


@login_required
def especies(request):
    especies = Especie.objects.all().order_by('descricao')

    context = {
        'especies': especies
    }

    return render(request, 'portal/especies.html', context)


@login_required
def my_pets(request):
    pets = Pet.objects.filter(user=request.user)

    context = {
        'pets': pets
    }

    return render(request, 'portal/my_pets.html', context)

def pet_show(request, slug):
    pet = get_object_or_404(Pet, slug=slug)

    context = {
        'pet': pet,
    }

    return render(request, 'portal/pet_show.html', context)

@login_required
def pet_new(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)

        if form.is_valid():
            pet = Pet()

            pet.user = request.user
            pet.nome = form.cleaned_data['nome']
            pet.especie = form.cleaned_data['especie']
            pet.raca = form.cleaned_data['raca']
            pet.foto = form.cleaned_data['foto']
            pet.status = 'Disponível'
            pet.idade = form.cleaned_data['idade']
            pet.genero = form.cleaned_data['genero']
            pet.descricao = form.cleaned_data['descricao']
            pet.uf = form.cleaned_data['uf']
            pet.cidade = form.cleaned_data['cidade']
            pet.contato = form.cleaned_data['contato']

            pet.save()

            return redirect('my_pets')

    form = PetForm()
    context = {
        'form': form,
    }

    return render(request, 'portal/pet_new.html', context)


@login_required
def pet_edit(request, slug):
    pet = get_object_or_404(Pet, slug=slug)

    if pet.user != request.user:
        return HttpResponseForbidden

    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet.nome = form.cleaned_data['nome']
            pet.especie = form.cleaned_data['especie']
            pet.raca = form.cleaned_data['raca']
            pet.foto = form.cleaned_data['foto']
            pet.idade = form.cleaned_data['idade']
            pet.genero = form.cleaned_data['genero']
            pet.descricao = form.cleaned_data['descricao']
            pet.uf = form.cleaned_data['uf']
            pet.cidade = form.cleaned_data['cidade']
            pet.contato = form.cleaned_data['contato']

            pet.save()
            return redirect('my_pets')

    form = PetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'portal/pet_edit.html', context)
