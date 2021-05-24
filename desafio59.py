# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Soma [2] multiplicar [3] maior [4]Digitar novos números [5] sair do programa
# Seu programa deverá realizar uma operação solicitada em cada caso.
menu = 0
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
while menu != 5:
    print(''' Opções do menu
    [1] Soma
    [2] Multiplicação
    [3] Maior
    [4] Digitar novos numeros
    [5] Sair do programa''')
    menu = int(input('\033[31mDigite a operação que deseja efetuar:\033[m '))
    if menu == 1:
        soma = num1 + num2
        print('A soma entre {} + {} = {}'.format(num1, num2, soma))
    elif menu == 2:
        mult = num1 * num2
        print('A multiplicação entre {} x {} = {}'.format(num1, num2, mult))
    elif menu == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior e {}'.format(num1, num2, maior))
    elif menu == 4:
        print('Digite os novos numeros')
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
    elif menu >= 6:
        print('Numero errado! por gentileza escolha as opções entre 1 e 5')
print('Fim do programa')
