# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para Binário
# - 2 para Octal
# - 3 para Hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] para Binário
[2] para Octal
[3] para Hexadecimal''')
dig = int(input('\033[1;31mDigite aqui:\033[m '))
if dig == 1:
    print('O número {} em Binário e \033[1;32m{}\033[m'.format(num, bin(num)[2:]))
elif dig == 2:
    print('O número {} em Octal e \033[1;32m{}\033[m'.format(num, oct(num)[2:]))
elif dig == 3:
    print('O número {} em Hexadecimal e \033[1;32m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente outra vez.')
