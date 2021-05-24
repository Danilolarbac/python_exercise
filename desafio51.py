# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre que os 10 primeiros termos
# dessa progressão. an = a +(n-1).r

t1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(1, 11):
    an = t1 + (c - 1)*r
    print(' {} '.format(an), end='→')
print(' Fim')
