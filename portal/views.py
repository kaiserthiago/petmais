from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from portal.forms import PetForm, ContatoForm, EspecieForm, RacaForm, PetQuestionForm, AnswerQuestionForm, InteresseForm
from portal.models import Pet, Contato, Especie, Raca, PetQuestion, PetAnswer, Interesse


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
    questions = PetQuestion.objects.filter(pet=pet).order_by('-created_at')

    form = PetQuestionForm()

    context = {
        'form': form,
        'pet': pet,
        'questions': questions,
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

            lista = Interesse.objects.filter(status='Solicitado')

            for item in lista:
                if (pet.especie == item.especie) and (pet.raca == item.raca):
                    subject, from_email, to = 'Pet Disponível - Pet+', 'thiagokaisi@gmail.com', item.user.email
                    text_content = 'This is an important message.'
                    html_content = '<p>This is an <strong>important</strong> message.</p>'
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()


                    # send_mail("Pet Disponível - Pet+",
                    #           msg+"Esta é uma mensagem automática, não é necessário respondê-la",
                    #           "thiagokaisi@gmail.com", [item.user.email], fail_silently=False)

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


@login_required
def pet_new_question(request, slug):
    pet = get_object_or_404(Pet, slug=slug)

    if request.method == 'POST':
        form = PetQuestionForm(request.POST)
        if form.is_valid():
            question = PetQuestion()

            question.user = request.user
            question.pet = pet
            question.question = form.cleaned_data['question']
            question.save()

    return redirect('pet_show', slug)


@login_required
def pet_question(request, slug):
    pet = get_object_or_404(Pet, slug=slug)

    context = {
        'pet': pet
    }

    return render(request, 'portal/pet_pergunta.html', context)


@login_required
def pet_answer_question(request, slug, question_id):
    pet = get_object_or_404(Pet, slug=slug)
    question = get_object_or_404(PetQuestion, pk=question_id)

    form = AnswerQuestionForm()

    if request.method == 'POST':
        form = AnswerQuestionForm(request.POST)
        if form.is_valid():
            pet_answer = PetAnswer()

            pet_answer.user = request.user
            pet_answer.answer = form.cleaned_data['answer']
            pet_answer.pet_question = question
            pet_answer.save()

            return redirect('pet_question', pet.slug)

    context = {
        'form': form,
        'pet': pet,
        'question': question
    }

    return render(request, 'portal/pet_resposta_pergunta.html', context)


@login_required
def interesses(request):
    interesses = Interesse.objects.filter(status='Solicitado')

    context = {
        'interesses': interesses
    }

    return render(request, 'portal/interesse.html', context)


@login_required
def interesse_new(request):
    if request.method == 'POST':
        form = InteresseForm(request.POST)

        if form.is_valid():
            interesse = Interesse()

            interesse.user = request.user
            interesse.especie = form.cleaned_data['especie']
            interesse.raca = form.cleaned_data['raca']
            interesse.idade = form.cleaned_data['idade']
            interesse.genero = form.cleaned_data['genero']

            interesse.save()

            subject, from_email, to = 'Cadastro de interesse - Pet+', 'thiagokaisi@gmail.com', request.user.email
            text_content = 'Olá, ' + request.user.first_name + '. Obrigado pelo seu interesse em adotar um Pet! Entraremos em contato quando encontrarmos seu novo Pet. Atenciosamente, Pet+ Seu portal de adoção de Pets.'
            html_content = '<p>Olá, ' + request.user.first_name + '.</p>' \
                                                                  'Obrigado pelo seu interesse em adotar um Pet!<br>' \
                                                                  'Entraremos em contato quando encontrarmos seu novo Pet.<br><br>' \
                                                                  '<p>Atenciosamente,</p>' \
                                                                  '<strong>Pet+</strong><br>' \
                                                                  '<em>Seu portal de adoção de Pets.</em><br><br>' \
                                                                  '<p style="color: red"><strong>Essa é uma mensagem automática, não é necessário respondê-la.</strong></p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return redirect('interesse_sucesso')

    form = InteresseForm()
    context = {
        'form': form,
    }
    return render(request, 'portal/interesse_new.html', context)


@login_required
def interesse_sucesso(request):
    return render(request, 'portal/interesse_success.html', {})
