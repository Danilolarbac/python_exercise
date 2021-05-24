#  Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
#  ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
gasto = c1 = c2 = menor = 0
barato = ' '
print('='*32)
print('{:-^40}'.format('\033[34mMERCADINHO DO ANTONY\033[m'))
print('='*32)
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço R$: '))
    gasto += preco
    c2 += 1
    if preco > 1000:
        c1 += 1
    if c2 == 1:  # pode ser escrito tbm if c2 == 1 or preco < menor: menor = preco barato = produto
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar a comprar?[S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'TOTAL = R${gasto:.2f}')
print(f'{c1} itens com valores maiores que R$1000')
print(f'{barato} e o item mais barato custando R${menor:.2f}')
