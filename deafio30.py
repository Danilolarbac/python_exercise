# Crie um programa que leia um número inteiro e mostre na tela se ele e Par ou Ímpar.

n = int(input('Digite um número: '))

if n % 2 == 0:
    print('{} é um numero Par'.format(n))
else:
    print('{} é um numero Ímpar'.format(n))
