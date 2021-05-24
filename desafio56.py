# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A media de idade do grupo.
# - Qual e o nome do homem mais velho.
# - Quantas mulheres tem menos de 20 anos.

soma = 0
maior = 0
cont = 0
cont1 = 0
media = 0
n = ''
for c in range(1, 5):
    print('------- {}ª Pessoa -------'.format(c))
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    soma += idade
    if sexo == 'M' and c == 1:
        maior = idade
        n = nome
    if idade > maior:
        maior = idade
        n = nome
    if sexo == 'F':
        cont += 1
        if idade < 20:
            cont1 += 1
media = soma / 4
print('A média de idade e {:.0f} anos'.format(media))
print('A maior idade e {} e o nome e {}'.format(maior, n))
print('Das {} mulheres cadastradas {} tem menos de 20 anos'. format(cont, cont1))
