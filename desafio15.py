# Escreva um programamque pregunte  a quantidade de km  percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$ 0.15 por km rodado.

q = float(input('Quantos quilômetros percorreu o carro?  '))
d = int(input('Quantos dias  o carro foi alugado?  '))

aluguel = (d * 60) + (q * 0.15)
print('Foram {} dias alugados com {} Km percorridos \nO total a pagar será R${:.2f} '.format(d, q, aluguel))
