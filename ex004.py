# Exercício referente a aula 6 do curso em vídeo

n = input('Digite algo em seu teclado: ')
print('O tipo primitivo e:', type(n))
print('Ele é um numero? {}'.format(n.isnumeric()))
print('Ele é alfabético? {}'.format(n.isalpha()))
print('Ele é alfanumérico? {}'.format(n.isalnum()))
print('Ele está em Maiúsculo? {}'.format(n.isupper()))
print('Ele está em minúsculo? {}'.format(n.islower()))
print('Ele pode ser impresso? {}'.format(n.isprintable()))
print('Ele só tem espaço? {}'.format(n.isspace()))
print('Ele é decimal? {}'.format(n.isdecimal()))
print('Ele está capitalizada? {}'.format(n.istitle()))
print('Ele é dígito ? {}'.format(n.isdigit()))
print('Ele é identifier? {}'.format(n.isidentifier())) #Ou seja, não pode começar com números ou conter espaços.
