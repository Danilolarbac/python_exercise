# Escreva um programa para aprovar um empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ele não
# pode exceder 30% do salário ou então a prestação será negada.

imovel = float(input('Qual o valor do imóvel que deseja adquirir:R$ '))
salario = float(input('Qual o seu salário para a simulação:R$ '))
anos = int(input('Em quantos anos deseja financiar o seu imóvel? '))

meses = anos * 12
prestacao = imovel / meses
tolerancia = salario * 0.30

if prestacao <= tolerancia:
    print('Sua prestação ficará R${:.2f} para pagar em {:.0f} meses, seu financiamento foi \033[1;4;34mAPROVADO\033[m '
          .format(prestacao, meses))
elif prestacao > tolerancia:
    print('Seu financiamento foi \033[1;4;31mNEGADO\033[m, pois o valor da prestação R${:.2f} excede 30% do salario de '
          'R${}'.format(prestacao, salario))
print('Muito obrigado por utilizar os serviços do nosso banco!')
