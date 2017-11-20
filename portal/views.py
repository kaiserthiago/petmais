from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from portal.forms import PetForm, ContatoForm
from portal.models import Pet, Contato


def home(request):
    return render(request, 'portal/home.html', {})


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


# @login_required
# def especie_new(request):
#     if request.method == 'POST':
#         form = EspecieForm(request.POST)
#
#         if form.is_valid():
#             especie = Especie()
#
#             especie.descricao = form.cleaned_data['descricao']
#
#             especie.save()
#
#             return redirect('my_especies')
#
#     form = EspecieForm()
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'portal/especie_new.html', context)
#
#
# @login_required
# def my_especies(request):
#     especies = Especie.objects.all().order_by('descricao')
#
#     context = {
#         'especies': especies
#     }
#
#     return render(request, 'portal/my_especies.html', context)


@login_required
def pet_new(request):
    if request.method == 'POST':
        form = PetForm(request.POST)

        if form.is_valid():
            pet = Pet()

            pet.user = request.user
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
            pet.status = 'Disponível'

            pet.save()

            return redirect('my_pets')

    form = PetForm()
    context = {
        'form': form,
    }

    return render(request, 'portal/pet_new.html', context)


@login_required
def my_pets(request):
    pets = Pet.objects.filter(user=request.user)

    context = {
        'pets': pets
    }

    return render(request, 'portal/my_pets.html', context)
