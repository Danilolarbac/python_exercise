# Melhore o desafio 61, perguntando pra o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
# disser que quer mostrar 0 termos

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = 1
total = 0
mais = 10
while mais != 0:
    total += mais  # total = total + mais
    while n <= total:
        print('{}'.format(a1), end=' ➡ ')
        a1 += r
        n += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} mostrado'.format(total))
