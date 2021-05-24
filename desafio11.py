# Faça um programa que leia a largura e altura de uma parede em metro, calcule a sua área e a quantidade de tinta
# nescessaria para pintala. Sabendo que cada litro de tinta, pinta uma área de 2m².

x = float(input('Qual a largura da parede? '))
y = float(input('Qual a altura da parede? '))

area = x * y  # Sabe-se que o cálculo de área se da pela equação A = Base x Altura
q = area / 2  # Sabe-se que com um litro de tinta pinta-se 2m².
print('A área da parede e {:.2f} m² e irá gastar {:.2f} L de tinta'.format(area, q))
