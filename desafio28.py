# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar
# descobrir qual foi o primeiro número escolhido pelo computador. o programa deverá escrever na tela se o usuário
# venceu ou ganhou.

from random import randint
from time import sleep
pc = randint(0, 5)  # Sorteia um numero entre 0 e 5
print('-=-'*20)
print('\033[0;31mVou pensar em um numero entre 0 e 5 e tente adivinhar...\033[m')
print('-=-'*20)
jogador = int(input('\033[1;34mEm que numero eu pensei?\033[m ')) # O jogador tenta adivinhar
print('\033[4;32mProcessando....\033[m')
sleep(3)
if jogador == pc:
    print('\033[46mParabéns! você conseguiu me vencer!\033[m')
else:
    print('Ganhei! eu pensei no numero \033[35m{}\033[m e não no \033[36m{}\033[m'.format(pc, jogador))


#from random import choice
#n = int(input('Digite um número entre 0 e 5: '))
#lista = [0, 1, 2, 3, 4, 5]
#npc = choice(lista)
#if n == npc:
 #   print('o Npc sorteou {} e vocês escolheu {} \nPortanto Você Ganhou'.format(npc, n))
#else:
 #   print('Voce perdeu pois, seu valor {} e diferente do que o Npc escolheu {}'.format(n, npc))
#print('Fim do jogo')
