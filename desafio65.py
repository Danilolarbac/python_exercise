# Crie um programa que leia varios numeros initeiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e menor valor lido. O programa deve perguntar ao usuario se ele ele quer ou não continuar
# a digitar valores
soma = c = maior = menor = 0
s = 'S'
while s in 'Ss':
    n = int(input('Digite um número: '))
    s = str(input('Quer continuar a digitar numeros[S/N]: ')).upper().strip()[0]
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / c
print('A média entre os {} numeros digitados e {}'.format(c, media))
print('O maior valor digita foi {} e o menor foi {}'.format(maior, menor))
