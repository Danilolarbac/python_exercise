from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
# Funções ceil e floor arredondam para cima ou para baixo o numero ex math.ceil() math.floor()
print('A raiz de {} e igual a {:.2f}'.format(num, floor(raiz)))
