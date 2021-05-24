# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
t = '\033[31mTABUADA\033[m'
print('-=-'*10)
print(f'{t:^35}')
print('-=-'*10)
while True:
    n = int(input('Digite um número(Negativo para PARAR): '))
    if n < 0:
        break
    for m in range(1, 11):
        print(f'{n} x {m:2} = {n*m}')
print('Acabou')
