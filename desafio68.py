# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
c = 0
while True:
    num = int(input('Qual o seu número: '))
    pc = randint(0, 10)
    soma = num + pc
    s = soma % 2
    e = ' '
    while e not in 'PI':
        e = str(input('Par ou Impar?[P ou I]: ')).upper().strip()[0]
    if s == 0 and e == 'P' or s == 1 and e == 'I':
        c += 1
        print(f'Você venceu! Você escolheu {num} e o pc escolheu {pc} e a soma deu {soma} que e', end=' ')
        print('par' if s == 0 else 'impar', end=' ')
        print('e você escolheu', end=' ')
        print('par' if e == 'P' else 'impar')
        print('\033[31m-\033[m'*40)
    else:
        print(f'Você perdeu! a soma deu {soma} que é', end=' ')
        print('par' if s == 0 else 'impar', end=' ')
        print(f'e você escolheu', end=' ')
        print('par' if e == 'P' else 'impar')
        break
    print('Vamos jogar novamente...')
print(f'Game Over! Você obteve {c} vitória consecultivas')
