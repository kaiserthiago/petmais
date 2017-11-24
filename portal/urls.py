from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^sobre$', views.sobre, name='sobre'),
    url(r'^contato$', views.contato, name='contato'),
    url(r'^interesse/sucesso', views.interesse_sucesso, name='interesse_sucesso'),
    url(r'^interesse/new', views.interesse_new, name='interesse_new'),
    url(r'^interesse', views.interesses, name='interesse'),

    url(r'^my_pets$', views.my_pets, name='my_pets'),
    url(r'^pet/show/(?P<slug>[-\w\d]+)$', views.pet_show, name='pet_show'),
    url(r'^pet/edit/(?P<slug>[-\w\d]+)$', views.pet_edit, name='pet_edit'),
    url(r'^pet/new$', views.pet_new, name='pet_new'),

    url(r'^pet/(?P<slug>[-\w\d]+)/perguntas/(?P<question_id>[\d]+)$', views.pet_answer_question, name='pet_answer_question'),
    url(r'^pet/nova/pergunta/(?P<slug>[-\w\d]+)$', views.pet_new_question, name='pet_new_question'),
    url(r'^pet/(?P<slug>[-\w\d]+)/perguntas$', views.pet_question, name='pet_question'),

    url(r'^especies$', views.especies, name='especies'),
    url(r'^especie/edit/(?P<slug>[-\w\d]+)$', views.especie_new, name='especie_edit'),
    url(r'^especie/new$', views.especie_new, name='especie_new'),

    url(r'^racas$', views.racas, name='racas'),
    url(r'^raca_edit/(?P<slug>[-\w\d]+)$', views.raca_new, name='raca_edit'),
    url(r'^raca/new$', views.raca_new, name='raca_new'),
]
