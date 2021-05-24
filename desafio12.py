# Faça um algoritimo que leia preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Informe o preço do produto: '))
print('O preço do produto e {:.2f} R$ e  com desconto de 5% fica por {:.2f} R$'.format(p, p - (p * 0.05)))
