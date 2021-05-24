# Refaça o desafio 009 mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laço for.
n = int(input('Digite um número para ver sua tabuada: '))
print('\033[1;34m='*15)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
print('\033[1;34m='*15)
