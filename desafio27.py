#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria Sousa
# primeiro = Ana
# ultimo = Sousa
nome = str(input('Digite o seu nome completo: ')).strip()
divide = nome.split()
print('Seu nome completo e: {}'.format(nome))
print('primeiro = {}'.format(divide[0]))
print('Ultimo = {}'.format(divide[len(divide)-1]))
