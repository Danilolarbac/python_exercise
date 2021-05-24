# Escreva um programa que leia dois números interios e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor e maior
# - O segundo valor e maior
# - Não exite valor maior, os dois são iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro número {} e maior que o segundo número {}'.format(num1, num2))
elif num1 < num2:
    print('O segundo numero {} e maior que o primeiro numero {}'.format(num2, num1))
else:
    print('Não existe um valor maior, o primeiro numero {} e igual ao segundo numero {}'.format(num1, num2))
