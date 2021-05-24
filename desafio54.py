# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas não atingiram a
# maioridade e quantas são maiores

from datetime import date
cont = 0
cont1 = 0
for c in range(1, 4):
    data = int(input('Em que ano a {}ª Pessoa nasceu? '.format(c)))
    idade = date.today().year - data
    if idade >= 18:
        cont += 1
    else:
        cont1 += 1
print('Das sete pessoas analisadas {} atingiram a maior idade e {} sao de menor'.format(cont, cont1))
