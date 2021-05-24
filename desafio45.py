# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep
print('''Vamos jogar Jokenpô? por gentileza escolha: 
 [0] pedra 
 [1] papel 
 [2] tesoura: ''')
jogador = int(input('Qual é a sua jogada? '))
print('Jo')
sleep(0.5)
print('ken')
sleep(0.5)
print('pô')
sleep(0.5)
itens = ('Pedra', 'Papel', 'Tesoura')
npc = randint(0, 2)
print('-=-'*10)
print('O computador jogou {}'.format(itens[npc]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=-'*10)
if npc == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada invalida')
elif npc == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogo invalido')
elif npc == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogo invalido')

# if npc == 0 and jogador == 2 or npc == 1 and jogador == 0 or npc == 2 and jogador == 1:
#    print('Você perdeu, pois {} vence {}'.format(itens[npc], itens[jogador]))
# elif jogador == 0 and npc == 2 or jogador == 1 and npc == 0 or jogador == 2 and npc == 0:
#    print('Você ganhou, pois {} vence {}'.format(itens[jogador], itens[npc]))
# else:
#    print('Empate, pois {} e igual {}'.format(itens[jogador], itens[npc]))
