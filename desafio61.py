# Refaça o desafio 51, lendo o primeiro temos e a razão de uma PA, mostre os 10 primeros termos da progressão usando a
# estrutura while. an = a1 +(n-1).r
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = 1
while n <= 10:
    print('{}'.format(a1), end=' ➡ ')
    a1 += r
    n += 1
print('Fim')

'''a1 = int(input('Digite o primeiro termo da PA: ')) # minha solução
r = int(input('Digite a razão da PA: '))
n = 1
while n != 11:
    an = a1 + (n-1)*r
    n += 1
    print('{}'.format(an), end=' ')
    print('➡' if n <= 10 else '➡ FIM', end=' ')'''
