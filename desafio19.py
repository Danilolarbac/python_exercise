# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome
# deles e escrevendo o nome escolhido.

from random import choice
a1 = input('Digite o nome do primeiro aluno ')
a2 = input('Digite o nome do segundo aluno  ')
a3 = input('Digite o nome do terceiro aluno ')
a4 = input('Digite o nome do quarto aluno   ')
lista = [a1, a2, a3, a4]
print('O aluno contemplado a apagar o quadro será {}'.format(choice(lista)))
