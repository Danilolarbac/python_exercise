# Crie um programa que leia quanto dinhero uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere do dolar a US$ 1.00 = R$ 3.27.

x = float(input('Quantos reais voçê possui? R$ '))
c = x / 3.27
print('Voçê tem {} R$ é pode comprar {:.2f} US$'.format(x, c))
