# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# - Á vista dinheiro/cheque: 10% de desconto
# - Á vista no cartão: 5% de desconto
# - Em ate 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros.
print('{:-^40}'.format(' LOJAS ANTONY GAMES '))
preco = float(input('Qual o valor de seu produto R$ '))
print(''' Formas de pagamento:
[1] Dinhero ou cheque 
[2] Á vista no cartão 
[3] Em até 2x no cartão 
[4] 3x ou mais no cartão''')
dig = int(input('Qual a forma de paramento? '))
if dig == 4 or dig == 3:
    if dig == 4:
        p = int(input('Quantas parcelas deseja dividir a compra? '))
        parcela = preco / p
        juros = (preco / p) * 0.2
        print('Seu pagamento foi em {} parcelas de R${} om juros, um total de R${} '
              .format(p, parcela + juros, p * (parcela + juros)))
    else:
        print('Seu pagamento foi em 2 parcelas sem juros de R${}, um total de R${}'.format(preco / 2, preco))
elif dig == 1:
    desconto = preco * 0.1
    print('Como o pagameneto foi a vista/ cheque seu desconto foi R${} e irá pagar R${}'
          .format(desconto, preco - desconto))
elif dig == 2:
    desconto = preco * 0.05
    print('Como o pagamento foi á vista no cartão seu desconto foi de R${} e irá pagar R${}'
          .format(desconto, preco - desconto))
else:
    print('Opção invalida de pagamento, tente novamente.')
