# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
from time import sleep

print('=' * 50)
print('Vamos verificar quais dos três numeros e o maior')
print('=' * 50)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro numero '))
print('Analisando...')
sleep(2)
# Verificando quem e o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
# Verificando quem e o maior
maior = n1
if n2 > n1 and n2 < n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))

'''if n1 > n2 and n1 > n3:
    print('{} É o maior valor'.format(n1))
    if n2 < n3:
        print('{} è o menor valor'.format(n2))
    else:
        print('{} É o menor valor'.format(n3))
if n2 > n1 and n2 > n3:
    print('{} É o maior valor'.format(n2))
    if n1 < n3:
        print('{} É o menor valor'.format(n1))
    else:
        print('{} É o menor valor'.format(n3))
if n3 > n1 and n3 > n2:
    print('{} É o maior valor'.format(n3))
    if n2 < n1:
        print('{} É o menor valor'.format(n2))
    else:
        print('{} É o menor valor'.format(n1))'''
