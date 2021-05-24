# Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
pc = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Digite um numero entre 0 e 10: '))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('O valor e maior, tente outra vez')
        elif jogador > pc:
            print('O valor e menor, tente outra vez')
print('Parabéns! acertou  com {} tentativas'.format(palpite))

# Programa feito por Danilo Cabral
# from random import randint
# palpites = 1
# pc = randint(0, 10)
# jogador = int(input('Digite um número entre 0 e 10: '))
# while jogador != pc:
#    if pc > jogador:
#        jogador = int(input('Você errou! o valor é MAIOR, tente outro palpite: '))
#    else:
#        jogador = int(input('Você errou! o valor é MENOR, tente outro palpite: '))
#    palpites = palpites + 1
# print('Seu numero foi {} e o do computador foi {}'.format(jogador, pc))
# print('Voce acertou! ao todo foram {} palpites para poder vencer'.format(palpites))
