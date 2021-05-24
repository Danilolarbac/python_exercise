# Crie um programa que leia varios numeros inteiros pelo teclado. O programa aso vai parar quando o usuario digitar o
# valor 999, que e a condição de parada. No final moste quantos numeros foram digitados e qual foi a soma entre
# eles(Desconsidrando o flag).

n = c = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print('Foram digitados {} números e sua soma é {}'.format(c, soma))
