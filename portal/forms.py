from django import forms

from portal.models import Raca, Especie, Pet, Contato


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('user', 'slug', 'status')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
            'especie': forms.Select(attrs={'class': 'form-control'}),
            'raca': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(),
            'idade': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Conte mais sobre o pet...'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'contato': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Como entrar em contato...'})

        }

        labels = {
            'nome': 'Nome',
            'especie': 'Espécie',
            'raca': 'Raça',
            'foto': 'Foto',
            'idade': 'Idade',
            'genero': 'Gênero',
            'descricao': 'Descrição',
            'uf': 'UF',
            'cidade': 'Cidade',
            'contato': 'Contato',
        }


class EspecieForm(forms.ModelForm):
    class Meta:
        model = Especie
        exclude = ('slug',)

        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'})
        }

        labels = {
            'descricao': 'Espécie',
        }


class RacaForm(forms.ModelForm):
    class Meta:
        model = Raca
        exclude = ('slug',)

        widgets = {
            'especie': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Selecione a espécie', 'autofocus': 'autofocus'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', })
        }

        labels = {
            'especie': 'Espécie',
            'descricao': 'Raça'
        }


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('user',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofcus'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Deixe aqui sua sugestão, crítica ou elogio.'})
        }

        labels = {
            'nome': 'Nome',
            'email': 'E-mail',
            'comentario': 'Comentário'
        }
