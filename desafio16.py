# Crie um programa q que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira. Ex: digite um
# numero: 6.127 ; O numero 6.127 tem a parte inteira 6.
# math.modf() separa a parte inteira da fracionada

"""from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira e {}'.format(num, trunc(num)))"""

num = float(input('Digite um valor: '))
print('O valor digitado e {} e a sua porção inteira e {}'.format(num,int(num)))
