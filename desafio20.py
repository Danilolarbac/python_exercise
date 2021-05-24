# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhosdos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
a1 = input('Aluno um: ')
a2 = input('Aluno dois ')
a3 = input('Aluno três ')
a4 = input('Aluno quatro ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será \n{}'.format(lista))
