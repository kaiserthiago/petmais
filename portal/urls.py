from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^sobre$', views.sobre, name='sobre'),
    url(r'^contato$', views.contato, name='contato'),

    url(r'^interesse/(?P<interesse_id>\d+)/adocao$', views.interesse_adocao, name='interesse_adocao'),
    url(r'^my_interesse/sucesso$', views.my_interesse_sucesso, name='my_interesse_sucesso'),
    url(r'^my_interesse/new$', views.my_interesse_new, name='my_interesse_new'),
    url(r'^my_interesse$', views.my_interesses, name='my_interesse'),

    url(r'^interesses$', views.interesses, name='interesses'),

    url(r'^dashboard$', views.dashboard, name='dashboard'),

    url(r'^conta$', views.minha_conta, name='minha_conta'),

    url(r'^my_pets$', views.my_pets, name='my_pets'),
    url(r'^pet/adocao/(?P<slug>[-\w\d]+)$', views.pet_adocao, name='pet_adocao'),
    url(r'^pet/show/(?P<slug>[-\w\d]+)$', views.pet_show, name='pet_show'),
    url(r'^pet/edit/(?P<slug>[-\w\d]+)$', views.pet_edit, name='pet_edit'),
    url(r'^pet/new$', views.pet_new, name='pet_new'),

    url(r'^pet/(?P<slug>[-\w\d]+)/perguntas/(?P<question_id>[\d]+)$', views.pet_answer_question, name='pet_answer_question'),
    url(r'^pet/nova/pergunta/(?P<slug>[-\w\d]+)$', views.pet_new_question, name='pet_new_question'),
    url(r'^pet/(?P<slug>[-\w\d]+)/perguntas$', views.pet_question, name='pet_question'),

    url(r'^especies$', views.especies, name='especies'),
    url(r'^especie/edit/(?P<slug>[-\w\d]+)$', views.especie_edit, name='especie_edit'),
    url(r'^especie/delete/(?P<slug>[-\w\d]+)$', views.especie_delete, name='especie_delete'),
    url(r'^especie/new$', views.especie_new, name='especie_new'),

    url(r'^racas$', views.racas, name='racas'),
    url(r'^raca/edit/(?P<slug>[-\w\d]+)$', views.raca_edit, name='raca_edit'),
    url(r'^raca/delete/(?P<slug>[-\w\d]+)$', views.raca_delete, name='raca_delete'),
    url(r'^raca/new$', views.raca_new, name='raca_new'),
]
