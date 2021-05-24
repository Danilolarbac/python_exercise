#  Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
#  a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. teste
print('=' * 40)
print('{:^40}'.format('Bank of Antony'))
print('='*40)
valor = int(input('Valor do saque:R$ '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('Saque efetuado! Obrigado por utilizar as Organizações ANTONY CABRAL')


# minha solução que não deu certo
'''while True:
    print('=' * 40)
    saque = int(input('Qual o valor do saque:R$ '))
    a = saque // 50
    b = saque / 50
    c = (b - a) * 50
    print('=' * 40, c)
    if b >= 1 and c == 0:
        print(f'{a} cédulas de 50R$')
    if b > 1:
        print(f'Total de {a} cédulas de 50R$')
    if c != 0:
        if c <= 10:
            print(' Total de 1 cédula de 10R$' if c == 10 else f'Total de {c} cédula de 1R$')
        if 10 < c <= 20:
            print('1 cédula de 20R$' if c == 20 else f'1 cédula de 10R$ é {c - 10:.0f} de 1R$')
        if 20 < c <= 30:
            print('1 cédula de 20R$', '1 de 10R$' if c == 30 else f'e {c - 20} de 1R$')
        if 30 < c <= 40:
            print(' 2 cédulas de 20R$' if c == 40 else f' 1 cédula de 20R$ 1 de 10R$ e {c - 30} de 1R$')
        if 40 < c <= 50:
            print('2 cedulas de 20 R$', '1 de 10R$' if c == 50 else f' e {c - 40} de 1R$')
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja fazer mais alguma operação?[S/N]: ')).upper().strip()[0]
    if r == 'N':
        break'''