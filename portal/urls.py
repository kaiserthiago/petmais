from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato', views.contato, name='contato'),
    url(r'^sobre$', views.sobre, name='sobre'),

    url(r'^my_pets$', views.my_pets, name='my_pets'),
    url(r'^pet_new$', views.pet_new, name='pet_new'),

    url(r'^my_especies$', views.my_especies, name='my_especies'),
    url(r'^especie_edit/(?P<slug>[-\w\d]+)$', views.especie_new, name='especie_edit'),
    url(r'^especie_new$', views.especie_new, name='especie_new'),
]