# Escreva um programa que converta uma temperatura digitando  em graus Celcius e convertentendo em Fahrenheit e Kevin.

c = float(input('Digite a temperatura em graus Celcius:ºC '))
f = (c * 9/5) + 32
k = c + 273.15
print('Dada a temperatura em {:.2f} ºC corresponde a {:.2f}ºf e a {:.2f} K'.format(c, f, k))
