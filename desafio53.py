# Crie um programa que leia uma frase qualquer e diga se ela e um palídromo, desconsiderando os espaços.
# ex: apos a sopa ; a sacada da casa; a torre da derrota; o lobo ama o bolo; anotaram a data da maratona

frase = input('Digite uma frase para saber se e um palíndromo: ').strip().upper()
frase = frase.split()  # frase.split() seguido de ''.join retira os espaços do meio da frase
frasejunta = ''.join(frase)
inverso = ''
for frase in range(len(frasejunta) - 1, - 1, - 1):
    inverso += frasejunta[frase]
print(' O inverso de {} é {}'.format(frasejunta, inverso))
if inverso == frasejunta:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palíndromo')

'''if frasejunta == frasejunta[::-1]:
    print('O inverso de \033[36m{}\033[m e \033[33m{}\033[m'.format(frasejunta, frasejunta[::-1]))
    print('Então ela e um palindromo')
else:
    print('O inversode \033[31m{}\033[m  e \033[31m{}\033[m'.format(frasejunta, frasejunta[::-1]))
    print('Não é um palindromo')'''
