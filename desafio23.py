# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um de seus digitos separados
# ex: digite o numero 1834
# unidade:4
# dezena:3
# centena:8
# milhas:1

num = int(input('Digite um numero: '))
u = num // 1 % 10  # Pega o numero e divide(//) por 1 depois por 10 e o resto(%) e o valor da unidade
d = num // 10 % 10  # Pega o numero e divide(//) por 10 depois por 10 e o resto(%) e o valor da dezena
c = num // 100 % 10  # Pega o numero e divide(//) por 100 depois por 10 e o resto(%) e o valor da centena
m = num // 1000 % 10  # Pega o numero e divide(//) por 100 depois por 10 e o resto(%) e o valor da milhar
print('Unidade:{} \nDezena:{} \nCentena:{} \nMilhar:{}'.format(u, d, c, m))
