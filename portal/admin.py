from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from portal.models import UserProfile, Raca, Especie, Pet, Contato, PetAnswer, PetQuestion


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


class RacaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'especie')
    list_filter = ['descricao', 'especie']


class EspecieAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao',)
    list_filter = ['descricao', ]


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'especie', 'raca', 'idade', 'genero', 'cidade', 'uf')
    list_filter = ['raca', 'idade', 'genero', 'cidade', 'uf']


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_filter = ['created_at', ]


class PetAnswerInline(admin.StackedInline):
    model = PetAnswer
    can_delete = False


class PetQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet', 'question', 'created_at')
    list_filter = ['pet', 'created_at']
    inlines = (PetAnswerInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Raca, RacaAdmin)
admin.site.register(Especie, EspecieAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(PetQuestion, PetQuestionAdmin)
