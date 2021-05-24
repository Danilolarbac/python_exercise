# Faça um programa  que leia um ângulo qualquer e mostre na tela  o valor do Seno, Cosseno e Tangente desse ângulo.
# Nesse caso e nescessario importa o modulo math.radians para transformar os ângulos para radianos.
from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo º '))
print('o valor do Seno = {:.2f} \nO valor do Cosseno = {:.2f} \nO valor da Tangente {:.2f}'.format(sin(radians(angulo)),
cos(radians(angulo)), tan(radians(angulo))))
