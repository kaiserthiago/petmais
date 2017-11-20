from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato', views.contato, name='contato'),
    url(r'^sobre$', views.sobre, name='sobre'),

    url(r'^my_pets$', views.my_pets, name='my_pets'),
    url(r'^pet_show/(?P<slug>[-\w\d]+)$', views.pet_new, name='pet_show'),
    url(r'^pet_edit/(?P<slug>[-\w\d]+)$', views.pet_edit, name='pet_edit'),
    url(r'^pet_new$', views.pet_new, name='pet_new'),

    url(r'^especies$', views.especies, name='especies'),
    url(r'^especie_edit/(?P<slug>[-\w\d]+)$', views.especie_new, name='especie_edit'),
    url(r'^especie_new$', views.especie_new, name='especie_new'),

    url(r'^racas$', views.racas, name='racas'),
    url(r'^raca_edit/(?P<slug>[-\w\d]+)$', views.raca_new, name='raca_edit'),
    url(r'^raca_new$', views.raca_new, name='raca_new'),
]