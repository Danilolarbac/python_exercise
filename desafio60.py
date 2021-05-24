# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# ex: 5!=5x4x3x2x1 = 120

n = int(input('Digite o número: '))
fat = n
f = 1
print('Calculando {}! ='.format(n), end=' ')
while fat != 0:
    print('{}'.format(fat), end=' ')
    print('x' if fat > 1 else '=', end=' ')
    f *= fat  # multiplicação / Divisão do fator nulo e sempre por 1 para evitar o 0
    fat -= 1  # subtrai sempre 1 do n
print('{}'.format(f), end=' ')
print('\nO fatoriral de {} é {}'.format(n, f))

# from math import factorial
# n = int(input('Digite o número:! '))
# print(factorial(n))
