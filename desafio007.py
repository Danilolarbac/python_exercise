# Desenvolva um programa que leia as notas do aluno, calcule e mostre a média.
x = float(input('Insira sua primeira nota: '))
y = float(input('Insira sua segunda nota: '))
z = float(input('Insira sua terceira nota: '))

media = (x + y + z) / 3
print('Sua média aritimética e: {:.1f}'.format(media))
