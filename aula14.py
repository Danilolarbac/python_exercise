# Estruturas de repetição while

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares é {} impares'.format(par, impar))

# r = 'S'
# while r == 'S':
#    n = int(input('Digite um valor: '))
#    r = str(input('Quer continuar? [S/N] ')).upper()
# print('Fim')

# n = 1
# while n != 0:  # flag condição de parada ponto de parada
#   n = int(input('Digite um valor: '))
# print('Fim')

# c = 1
# while c < 10:  # Enquanto contador for menos que 10
#   print(c, end=' ')
#   c =c + 1
# print('Fim')

# for c in range(1, 10):
#    print(c, end=' ')
# print('Fim')
