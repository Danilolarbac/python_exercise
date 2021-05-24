n1 = int(input('um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# { :.3f significa que esse produto so tera tres casas decimais flutuante(float)}
# ,end= junta os dois prints na mesma linha
# Para quebra a linha \n

print('A soma é {}, \n O produto é {}, \n a divisão e {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira é {}, A potêcia é {}'.format(di, e))
