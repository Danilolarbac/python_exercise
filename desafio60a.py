# Faça um programa que leia um numero qualquer e mostre o seu fatorial. Utilizando a função for
# ex: 5!=5x4x3x2x1 = 120

n = int(input('Digite um número: '))
fat = n
f = 1
print('Calculando \033[31m{}!\033[m ='.format(n), end=' ')
for fat in range(n, 0, -1):
    print('{}'.format(fat), end=' ')
    print('x' if fat > 1 else '=', end=' ')
    f *= fat
    fat -= 1
print('{}'.format(f))