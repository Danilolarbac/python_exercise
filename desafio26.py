# Faça um programa que leia uma frase pelo teclado e mostre:
# a) Quantas vezes aparece a letra "A"
# b) Em que posição ela aparece a primeira vez
# c) Em que posição ela aparece a ultima vez

frase = str(input('Escreva uma frase qualquer: ')).strip().upper()

print('Aparecem {} letras A'.format(frase.count('A')))
print('A letra A aparece primeiro na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}'. format(frase.rfind('A')+1))
