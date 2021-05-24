# Crie um programa que mostre o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiusculas
# b) O nome com todas as letras minusculas
# c) Quantas letras ao todo(sem considerar espaços)
# d) Quantas letras tem o primeiro nome:

nome = str(input('Digite o seu nome completo: ')).strip()
x = (len(nome))-(nome.count(' '))
y = nome.split()
print('O nome com todas as letras maiusculas: {}'.format(nome.upper()))
print('O nome com todas as letras minusculas {}'.format(nome.lower()))
print('o nome tem {} letras'.format(x))
# print('O Primeiro nome tem {} letras'.format(nome.find(' ')))
print('O Primeiro nome que e {} e tem {} letras'.format(y[0], len(y[0])))
