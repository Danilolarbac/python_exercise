# Escreva um programa que leia a velocidade de um carro. SE ele ultrapassar 80 Km/h, mostre um mensagem dizendo que ele
# foi multado. A multa vai custar R$7.00 por cada Km acima do limite.

vm = float(input('Qual a velocidade média (km/h) do seu carro? '))
cores = {'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'pretoebranco' : '\033[7;30',
         'limpa' : '\033[m'}
if vm > 80:
    multa = (vm - 80) * 7
    print('Seu carro foi multado e a multa e de {}R${:.2f}{}'.format(cores['vermelho'], multa, cores['limpa']))
print('{}Tenha um boma dia dirija com segurança{}'.format(cores['azul'], cores['limpa']))
