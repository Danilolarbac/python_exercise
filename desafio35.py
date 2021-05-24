# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não forma um triângulo.
print('-=-'*11)
print('Analisador de Trirângulos')
print('-=-'*11)
a = float(input('Insira o comprimento da reta a: '))
b = float(input('Insira o comprimento da reta b: '))
c = float(input('Insira o comprimento da reta c: '))

if a < b + c and b < a + c and c < a + b:
    print('suas retas {}, {} e {} podem forma um triângulo'.format(a, b, c))
else:
    print('Elas não podem formar um triângulo')
