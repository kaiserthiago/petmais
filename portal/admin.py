from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from portal.models import UserProfile, Raca, Especie, Pet


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


class RacaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'especie')
    list_filter = ['descricao', 'especie']


class EspecieAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    list_filter = ['descricao', ]


class PetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'raca', 'idade', 'genero', 'cidade', 'uf')
    list_filter = ['raca', 'idade', 'genero', 'cidade', 'uf']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Raca, RacaAdmin)
admin.site.register(Especie, EspecieAdmin)
admin.site.register(Pet, PetAdmin)
