somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª Pessoa ------'.format(p))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input("Sexo[M/F]: ").strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos é se chama {}'.format(maioridadehomem, nomevelho))
print('O número de mulheres abaixo dos 20 anos é {}'.format(totmulher20))
