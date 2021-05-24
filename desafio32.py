# Faça um programa que leia um ano qualquer e dia se ele é Bissexto.
from datetime import date
a = int(input('Qual ano você quer analizae? Coloque 0 para analizar o ano atual: '))
if a == 0:
    a = date.today().year  # essa instrução date.today().year pega o ano atual da maquina.
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é Bissexto'.format(a))
else:
    print('O ano {} não é Bissexto'.format(a))
