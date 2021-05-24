# Faça um programa que leia um numero inteiro e diga se ele e ou não um número primo.

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[31m', end='')
        tot += 1
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Ele é primo')
else:
    print('ele não é primo')
