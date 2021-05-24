# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por
# Km para viagens de até 200 Km e R$0.45 para viagens mais longas.

d = float(input('Qual a diatância percorrida: '))

print('Como a distância percorrida foi {} Km'.format(d))
preço = d * 0.50 if d <= 200 else d * 0.45
#if d <= 200:
 #   preco = d * 0.50
#else:
 #   preco = d *0.45
print('O preço da sua passagem será {:.2f}'.format(preço))
