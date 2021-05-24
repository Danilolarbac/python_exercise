# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for impar, desconsidere-o.
s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma dos {} numeros pares  e {}'.format(cont, s))
