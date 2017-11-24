from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from portal.models import Interesse


# def verifica_interesse(especie, raca):
#     lista = get_object_or_404(Interesse, status='Disponível')
#
#     for item in lista:
#         if (especie == lista.especie) and (raca == lista.raca):
#             send_mail("Pet Disponível",
#                       "Teste de e-email enviado automático. Por favor não responda",
#                       "thiagokaisi@gmail.com", [item.user.email], fail_silently=False)