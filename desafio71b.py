print('-' * 30)
print('{:^30}'.format('BANK OF HERIKA'))
print('-' * 30)
saque = int(input('Qual o valor do saque:R$ '))
total = saque
ced = 100
c = 0
while True:
    if total >= ced:
        total -= ced
        c += 1
    else:
        if c > 0:
            print(f'O total de {c} cedulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        c = 0
        if total == 0:
            break
print('Obrigado por usar os serviços do nosso banco')
