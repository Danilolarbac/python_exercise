# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
c1 = c2 = c3 = 0
while True:
    idade = int(input('Digite a idade: '))
    genero = ' '
    resposta = ' '
    while genero not in 'MF':
        genero = str(input('Digite o gênero[M/F]: ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar a cadastrar [S/N]? ')).upper().strip()[0]
    print('='*40)
    if idade >= 18:
        c1 += 1
    if genero == 'M':
        c2 += 1
    if genero == 'F' and idade <= 20:
        c3 += 1
    if resposta == 'N':
        break
print(f'{c1} pessoas tem mais de 18 anos')
print(f'{c2} homens foram cadastrados')
print(f'{c3} mulheres tem menos de 20 anos')
